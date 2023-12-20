from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper import directory, file
from _helper.timeout import reset_to_not_timed_out
from py.path import local

from browserist import Browser, BrowserSettings, factory
from browserist.constant import idle_timeout
from browserist.exception.download import (DownloadHandlerMultipleFinalFilesError,
                                           DownloadHandlerMultipleTemporaryFilesError)
from browserist.model.download.handler import DownloadHandler


def get_download_handler(browser: Browser, download_dir_entries_before_download: list[str]) -> DownloadHandler:
    def ensure_uses_temporary_file_is_true(download_handler: DownloadHandler) -> DownloadHandler:
        property(
            fget=lambda value: True,
            fset=setattr(download_handler, "_uses_temporary_file.setter", lambda: True),
            fdel=None
        )
        return download_handler

    download_handler = factory.get.download_handler(
        browser_driver=browser._browser_driver,
        download_dir_entries_before_download=download_dir_entries_before_download,
        idle_download_timeout=idle_timeout.VERY_SHORT,
    )
    return ensure_uses_temporary_file_is_true(download_handler)


@pytest.mark.parametrize("number_of_files, expectation", [
    (0, does_not_raise()),
    (1, does_not_raise()),
    (2, pytest.raises(DownloadHandlerMultipleTemporaryFilesError)),
])
def test_download_handler_expection_for_multiple_temporary_files(number_of_files: int, expectation: Any, tmpdir: local) -> None:
    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with Browser(brower_settings) as browser:
        browser = reset_to_not_timed_out(browser)
        download_dir_entries_before_download = []
        download_handler = get_download_handler(browser, download_dir_entries_before_download)
        file.create_multiple(download_dir, f"txt{download_handler._temporary_file_extension}", number_of_files)
        with expectation:
            _ = download_handler._attempt_to_get_temporary_file() is not None


@pytest.mark.parametrize("number_of_files, expectation", [
    (0, does_not_raise()),
    (1, does_not_raise()),
    (2, pytest.raises(DownloadHandlerMultipleFinalFilesError)),
])
def test_download_handler_expection_for_multiple_final_files(number_of_files: int, expectation: Any, tmpdir: local) -> None:
    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with Browser(brower_settings) as browser:
        browser = reset_to_not_timed_out(browser)
        download_dir_entries_before_download = []
        download_handler = get_download_handler(browser, download_dir_entries_before_download)
        file.create_multiple(download_dir, "txt", number_of_files)
        with expectation:
            _ = download_handler._attempt_to_get_final_file(download_dir_entries_before_download) is not None
