from contextlib import nullcontext as does_not_raise
from pathlib import Path
from typing import Any

import pytest
from _fixture.download_handler import get as get_download_handler
from _helper import directory, file
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser, BrowserSettings
from browserist.exception.download import (DownloadHandlerMultipleFinalFilesError,
                                           DownloadHandlerMultipleTemporaryFilesError)


@pytest.mark.parametrize("number_of_files, expectation", [
    (0, does_not_raise()),
    (1, does_not_raise()),
    (2, pytest.raises(DownloadHandlerMultipleTemporaryFilesError)),
])
def test_download_handler_expection_for_multiple_temporary_files(number_of_files: int, expectation: Any, tmpdir: Path) -> None:
    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    browser_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with Browser(browser_settings) as browser:
        browser = reset_to_not_timed_out(browser)
        download_dir_entries_before_download = []
        download_handler = get_download_handler(browser, download_dir_entries_before_download, uses_temporary_file=True)
        file.create_multiple(download_dir, f"txt{download_handler._temporary_file_extension}", number_of_files)
        with expectation:
            _ = download_handler._attempt_to_get_temporary_file() is not None


@pytest.mark.parametrize("number_of_files, expectation", [
    (0, does_not_raise()),
    (1, does_not_raise()),
    (2, pytest.raises(DownloadHandlerMultipleFinalFilesError)),
])
def test_download_handler_expection_for_multiple_final_files(number_of_files: int, expectation: Any, tmpdir: Path) -> None:
    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    browser_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with Browser(browser_settings) as browser:
        browser = reset_to_not_timed_out(browser)
        download_dir_entries_before_download = []
        download_handler = get_download_handler(browser, download_dir_entries_before_download, uses_temporary_file=True)
        file.create_multiple(download_dir, "txt", number_of_files)
        with expectation:
            _ = download_handler._attempt_to_get_final_file() is not None
