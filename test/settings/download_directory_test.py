import os
import time

import pytest
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings
from browserist.constant.directory import DOWNLOADS_DIR

BROWSER_SETTINGS_WITH_DEFAULT_DOWNLOAD_DIR = BrowserSettings(
    headless=True
)

BROWSER_SETTINGS_WITH_SET_DEFAULT_DOWNLOAD_DIR = BrowserSettings(
    headless=True,
    download_dir=DOWNLOADS_DIR
)

CUSTOM_DOWNLOAD_DIR = os.path.join(DOWNLOADS_DIR, "test")

BROWSER_SETTINGS_WITH_CUSTOM_DOWNLOAD_DIR = BrowserSettings(
    headless=True,
    download_dir=CUSTOM_DOWNLOAD_DIR
)

EXPECTED_DOWNLOADED_FILE_NAME = "file.zip"


@pytest.mark.parametrize("browser_settings", [
    BROWSER_SETTINGS_WITH_DEFAULT_DOWNLOAD_DIR,
    BROWSER_SETTINGS_WITH_SET_DEFAULT_DOWNLOAD_DIR,
    BROWSER_SETTINGS_WITH_CUSTOM_DOWNLOAD_DIR,
])
def test_download_directory_is_created_if_does_not_exist(browser_settings: BrowserSettings) -> None:
    with Browser(browser_settings):
        assert os.path.exists(browser_settings._download_dir)


@pytest.mark.parametrize("browser_settings", [
    BROWSER_SETTINGS_WITH_DEFAULT_DOWNLOAD_DIR,
    BROWSER_SETTINGS_WITH_SET_DEFAULT_DOWNLOAD_DIR,
    BROWSER_SETTINGS_WITH_CUSTOM_DOWNLOAD_DIR,
])
def test_download_directory_is_file_downloaded(browser_settings: BrowserSettings) -> None:
    with Browser(browser_settings) as browser:
        directory_items_before_download = len(os.listdir(browser_settings._download_dir))
        browser.open.url(internal_url.DOWNLOAD)
        browser.click.button("//button[@id='download']")
        attempts = 0
        while len(os.listdir(browser_settings._download_dir)) == directory_items_before_download and attempts < 10:
            time.sleep(0.1)
            attempts += 1
        assert len(os.listdir(browser_settings._download_dir)) == directory_items_before_download + 1
        assert EXPECTED_DOWNLOADED_FILE_NAME in os.listdir(browser_settings._download_dir)
        if EXPECTED_DOWNLOADED_FILE_NAME in os.listdir(browser_settings._download_dir):
            file_path = os.path.join(browser_settings._download_dir, EXPECTED_DOWNLOADED_FILE_NAME)
            os.remove(file_path)
