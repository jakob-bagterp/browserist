import time
from contextlib import nullcontext as expectation_of_no_exceptions_raised
from pathlib import Path
from threading import Thread

import pytest
from _fixture.download_handler import get as get_download_handler
from _helper import directory, file
from _helper.python import is_python_version
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser, BrowserSettings, BrowserType
from browserist.helper import operating_system

FINAL_FILE_NAME = "file.txt"
PRELIMINARY_TEMPORARY_FILE_NAME = ".com.google.Chrome.1a2b3c"
TEMPORARY_FILE_EXTENSION = ".crdownload"
TEMPORARY_FILE_NAME = f"{FINAL_FILE_NAME}{TEMPORARY_FILE_EXTENSION}"


class SimulateFileDownloadInStagesThread(Thread):
    """NB: This is only intended to work for Chrome and Edge."""

    def __init__(self, download_dir: str, preliminary_temporary_file_time: float, temporary_file_time: float) -> None:
        Thread.__init__(self)
        self.download_dir = download_dir
        self.preliminary_temporary_file_time = preliminary_temporary_file_time
        self.temporary_file_time = temporary_file_time
        self._download_dir_path = Path(self.download_dir)
        self._preliminary_temporary_file_path = self._download_dir_path / PRELIMINARY_TEMPORARY_FILE_NAME
        self._final_file_path = self._download_dir_path / FINAL_FILE_NAME
        self._temporary_file_path = self._download_dir_path / TEMPORARY_FILE_NAME

    def run(self) -> None:
        if self.preliminary_temporary_file_time > 0:
            file.create(self._preliminary_temporary_file_path)
            time.sleep(self.preliminary_temporary_file_time)
            self._preliminary_temporary_file_path.rename(self._temporary_file_path)
        else:
            file.create(self._temporary_file_path)
        time.sleep(self.temporary_file_time)
        self._temporary_file_path.rename(self._final_file_path)


class DownloadHandlerThread(Thread):
    def __init__(self, browser: Browser, download_dir_entries_before_download: list[str], uses_temporary_file: bool) -> None:
        Thread.__init__(self)
        self.browser = browser
        self.download_dir_entries_before_download = download_dir_entries_before_download
        self.uses_temporary_file = uses_temporary_file

    def run(self) -> None:
        download_handler = get_download_handler(self.browser, self.download_dir_entries_before_download, self.uses_temporary_file)
        _ = download_handler.await_and_get_final_file()
        assert download_handler._final_file is not None
        assert download_handler._final_file.name == FINAL_FILE_NAME
        if download_handler._temporary_file is not None:
            assert download_handler._temporary_file.name == TEMPORARY_FILE_NAME


@pytest.mark.parametrize("preliminary_temporary_file_time, temporary_file_time", [
    (0, 0),
    (0, 0.1),
    (0, 0.2),
    (0, 1),
    (0.01, 0),
    (0.01, 0.1),
    (0.01, 0.2),
    (0.01, 1),
    (0.1, 0),
    (0.1, 0.1),
    (0.1, 0.2),
    (0.1, 1),
    (0.2, 0),
    (0.2, 0.1),
    (0.2, 0.2),
    (0.2, 1),
])
@pytest.mark.filterwarnings("error::pytest.PytestUnhandledThreadExceptionWarning")
def test_simulate_file_download_in_timed_stage_scenarios_for_download_handler(preliminary_temporary_file_time: float, temporary_file_time: float, tmpdir: Path) -> None:
    """Test behaviour of `DownloadHandler` concurrently with simulation of the download file when it changes from preliminary to temporary to final file."""

    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    browser_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    if browser_settings.type not in [BrowserType.CHROME, BrowserType.EDGE]:
        pytest.skip(f"Timing tests for DownloadHandler are only supported by Chrome and Edge, not {browser_settings.type}.")
    if operating_system.is_windows() and is_python_version(3, 13):  # TODO: Remove this once we have a fix for this exception.
        pytest.skip("When Python 3.13 runs on Windows there are inconstencies in the timing of temporary and final file names.")

    with Browser(browser_settings) as browser:
        with expectation_of_no_exceptions_raised():
            browser = reset_to_not_timed_out(browser)
            download_dir_entries_before_download = []
            threads: list[Thread] = []

            if browser_settings.type is BrowserType.EDGE:
                preliminary_temporary_file_time = 0  # Edge does not create a preliminary temporary file, which otherwise may create issues in the download file simulation.
            simulate_file_download_thread = SimulateFileDownloadInStagesThread(download_dir, preliminary_temporary_file_time, temporary_file_time)
            simulate_file_download_thread.start()
            threads.append(simulate_file_download_thread)

            download_handler_thread = DownloadHandlerThread(browser, download_dir_entries_before_download, uses_temporary_file=True)
            download_handler_thread.start()
            threads.append(download_handler_thread)

            for thread in threads:
                thread.join()
