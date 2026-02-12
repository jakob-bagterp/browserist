import os

import pytest

from browserist import Browser, BrowserSettings, helper_download
from browserist.constant.directory import DOWNLOADS_DIR

TEST_FILE_NAME = "test.txt"


@pytest.mark.parametrize(
    "download_dir, file_name, expected_file_path",
    [(DOWNLOADS_DIR, TEST_FILE_NAME, os.path.join(DOWNLOADS_DIR, TEST_FILE_NAME))],
)
def test_helper_download_get_file_path(download_dir: str, file_name: str, expected_file_path: str) -> None:
    browser_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with Browser(browser_settings) as browser:
        assert helper_download.get_file_path(browser._browser_driver, file_name) == expected_file_path
