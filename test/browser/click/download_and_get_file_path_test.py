import os

from _constant import download_page
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from py.path import local

from browserist import Browser, BrowserSettings


def test_click_download_and_get_file_path(tmpdir: local) -> None:
    download_dir = os.path.join(str(tmpdir), "downloads")
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir)
    with Browser(brower_settings) as browser:
        reset_to_not_timed_out(browser)
        browser.open.url(internal_url.DOWNLOAD)
        assert browser.click.download_and_get_file_path("//button[@id='download']").name == download_page.EXPECTED_FILE_NAME
