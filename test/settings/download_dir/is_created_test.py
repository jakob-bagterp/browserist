import os

import pytest

from browserist import Browser, BrowserSettings
from browserist.constant.directory import DOWNLOADS_DIR

BROWSER_SETTINGS_WITH_DEFAULT_DOWNLOAD_DIR = BrowserSettings(headless=True, check_connection=False)

BROWSER_SETTINGS_WITH_SET_DEFAULT_DOWNLOAD_DIR = BrowserSettings(
    headless=True, download_dir=DOWNLOADS_DIR, check_connection=False
)

CUSTOM_DOWNLOAD_DIR = os.path.join(DOWNLOADS_DIR, "test")

BROWSER_SETTINGS_WITH_CUSTOM_DOWNLOAD_DIR = BrowserSettings(
    headless=True, download_dir=CUSTOM_DOWNLOAD_DIR, check_connection=False
)


@pytest.mark.parametrize(
    "browser_settings",
    [
        BROWSER_SETTINGS_WITH_DEFAULT_DOWNLOAD_DIR,
        BROWSER_SETTINGS_WITH_SET_DEFAULT_DOWNLOAD_DIR,
        BROWSER_SETTINGS_WITH_CUSTOM_DOWNLOAD_DIR,
    ],
)
def test_download_directory_is_created_if_not_exists(browser_settings: BrowserSettings) -> None:
    with Browser(browser_settings):
        assert os.path.exists(browser_settings._download_dir)
