import os
import time

import pytest
from _mock_data.url import internal_url
from pytest import TempPathFactory

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


@pytest.mark.parametrize("browser_settings", [
    BROWSER_SETTINGS_WITH_DEFAULT_DOWNLOAD_DIR,
    BROWSER_SETTINGS_WITH_SET_DEFAULT_DOWNLOAD_DIR,
    BROWSER_SETTINGS_WITH_CUSTOM_DOWNLOAD_DIR,
])
def test_download_directory_is_created_if_does_not_exist(browser_settings: BrowserSettings) -> None:
    with Browser(browser_settings):
        assert os.path.exists(browser_settings._download_dir)


EXPECTED_DOWNLOADED_FILE_NAME = "file.zip"


def test_download_directory_is_file_downloaded(tmp_path_factory: TempPathFactory) -> None:
    def wait_for_download_to_finish(browser_settings: BrowserSettings, directory_items_before_download: int) -> None:
        attempts = 0
        while get_directory_items_count(browser_settings._download_dir) == directory_items_before_download and attempts < 10:
            time.sleep(0.1)
            attempts += 1

    def clean_up_downloaded_file(file_path: str) -> None:
        if EXPECTED_DOWNLOADED_FILE_NAME in get_directory_items(browser_settings._download_dir):
            os.remove(file_path)

    def get_directory_items(path: str) -> list[str]:
        return os.listdir(path)

    def get_directory_items_count(path: str) -> int:
        return len(get_directory_items(path))

    temp_download_dir = tmp_path_factory.mktemp("downloads") / "test"
    os.mkdir(temp_download_dir)  # TODO: This is a strange workaround to make the test pass. Investigate.
    browser_settings = BrowserSettings(
        headless=True,
        download_dir=temp_download_dir
    )

    with Browser(browser_settings) as browser:
        directory_items_before_download = get_directory_items_count(browser_settings._download_dir)
        browser.open.url(internal_url.DOWNLOAD)
        browser.click.button("//button[@id='download']")
        wait_for_download_to_finish(browser_settings, directory_items_before_download)
        assert get_directory_items_count(browser_settings._download_dir) == directory_items_before_download + 1
        assert EXPECTED_DOWNLOADED_FILE_NAME in get_directory_items(browser_settings._download_dir)
        file_path = os.path.join(browser_settings._download_dir, EXPECTED_DOWNLOADED_FILE_NAME)
        assert os.path.isfile(file_path)
        assert os.path.getsize(file_path) > 0
        clean_up_downloaded_file(file_path)
