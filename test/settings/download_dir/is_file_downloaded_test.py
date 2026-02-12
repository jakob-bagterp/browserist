import os
import time
from pathlib import Path

import pytest
from _constant import download_page
from _helper import directory
from _mock_data.url import internal_url
from _mock_data.xpath.download_page import DONWLOAD_BUTTON_XPATH

from browserist import Browser, BrowserSettings


@pytest.mark.parametrize("download_dir", ["downloads"])
def test_download_directory_is_file_downloaded(download_dir: str, tmpdir: Path) -> None:
    def wait_for_download_to_finish(browser_settings: BrowserSettings, directory_items_before_download: int) -> None:
        timeout_seconds = 5
        interval_seconds = 0.1
        total_attempts = int(timeout_seconds / interval_seconds)
        attempt = 0
        while (
            get_directory_items_count(browser_settings._download_dir) == directory_items_before_download
            and attempt < total_attempts
        ):
            time.sleep(interval_seconds)
            attempt += 1

    def clean_up_downloaded_file(file_path: str) -> None:
        if download_page.EXPECTED_FILE_NAME in get_directory_items(browser_settings._download_dir):
            os.remove(file_path)

    def get_directory_items(path: str) -> list[str]:
        return os.listdir(path)

    def get_directory_items_count(path: str) -> int:
        return len(get_directory_items(path))

    browser_settings: BrowserSettings = BrowserSettings(
        headless=True, download_dir=directory.create_and_get_temporary(tmpdir, download_dir), check_connection=False
    )

    with Browser(browser_settings) as browser:
        directory_items_before_download = get_directory_items_count(browser_settings._download_dir)
        browser.open.url(internal_url.DOWNLOAD)
        browser.click.button(DONWLOAD_BUTTON_XPATH)
        wait_for_download_to_finish(browser_settings, directory_items_before_download)
        assert get_directory_items_count(browser_settings._download_dir) == directory_items_before_download + 1
        assert download_page.EXPECTED_FILE_NAME in get_directory_items(browser_settings._download_dir)
        file_path = os.path.join(browser_settings._download_dir, download_page.EXPECTED_FILE_NAME)
        assert os.path.isfile(file_path)
        assert os.path.getsize(file_path) > 0
        clean_up_downloaded_file(file_path)
