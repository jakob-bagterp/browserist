import time
from contextlib import nullcontext as expectation_of_no_exceptions_raised
from pathlib import Path
from threading import Thread

import pytest
from _fixture.download_handler import get as get_download_handler
from _helper import directory, file
from _helper.timeout import reset_to_not_timed_out
from py.path import local

from browserist import Browser, BrowserSettings, BrowserType

FINAL_FILE_NAME = "file.txt"


class SimulateFileDownloadInStagesThread(Thread):
    """NB: This is only intended to work for Chrome and Edge."""

    _preliminary_temporary_file_name = ".com.google.Chrome.1a2b3c"
    _temporary_file_extension = ".crdownload"
    _temporary_file_name = f"{FINAL_FILE_NAME}{_temporary_file_extension}"

    def __init__(self, download_dir: str, preliminary_temporary_file_time: float, temporary_file_time: float) -> None:
        Thread.__init__(self)
        self.download_dir = download_dir
        self.preliminary_temporary_file_time = preliminary_temporary_file_time
        self.temporary_file_time = temporary_file_time
        self._download_dir_path = Path(self.download_dir)
        self._preliminary_temporary_file_path = self._download_dir_path / self._preliminary_temporary_file_name
        self._final_file_path = self._download_dir_path / FINAL_FILE_NAME
        self._temporary_file_path = self._download_dir_path / self._temporary_file_name

    def run(self) -> None:
        file.create(self._preliminary_temporary_file_path)
        time.sleep(self.preliminary_temporary_file_time)
        self._preliminary_temporary_file_path.rename(self._temporary_file_path)
        time.sleep(self.temporary_file_time)
        self._temporary_file_path.rename(self._final_file_path)


class TestDownloadHandlerThread(Thread):
    def __init__(self, browser: Browser, download_dir_entries_before_download: list[str], uses_temporary_file: bool) -> None:
        Thread.__init__(self)
        self.browser = browser
        self.download_dir_entries_before_download = download_dir_entries_before_download
        self.uses_temporary_file = uses_temporary_file

    def run(self) -> None:
        download_handler = get_download_handler(self.browser, self.download_dir_entries_before_download, self.uses_temporary_file)
        assert download_handler.await_and_get_final_file().name == FINAL_FILE_NAME


@pytest.mark.parametrize("preliminary_temporary_file_time, temporary_file_time", [
    (0, 0),
    (0, 0.1),
    (0, 0.2),
    (0, 1),
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
def test_simulate_file_download_in_timed_stage_scenarios_for_download_handler(preliminary_temporary_file_time: float, temporary_file_time: float, tmpdir: local) -> None:
    """Test behaviour of `DownloadHandler` concurrently with simulation of the download file when it changes from preliminary to temporary to final file."""

    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    if brower_settings.type not in [BrowserType.CHROME, BrowserType.EDGE]:
        pytest.skip(f"Timing tests for DownloadHandler are only supported by Chrome and Edge, not {brower_settings.type}.")

    with Browser(brower_settings) as browser:
        with expectation_of_no_exceptions_raised():
            browser = reset_to_not_timed_out(browser)
            download_dir_entries_before_download = []
            threads: list[Thread] = []

            simulate_file_download_thread = SimulateFileDownloadInStagesThread(download_dir, preliminary_temporary_file_time, temporary_file_time)
            simulate_file_download_thread.start()
            threads.append(simulate_file_download_thread)

            download_handler_thread = TestDownloadHandlerThread(browser, download_dir_entries_before_download, uses_temporary_file=True)
            download_handler_thread.start()
            threads.append(download_handler_thread)

            for thread in threads:
                thread.join()
