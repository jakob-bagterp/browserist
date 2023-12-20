from _constant import download_page
from _helper import directory
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath import xpath
from py.path import local

from browserist import Browser, BrowserSettings


def test_click_download_and_get_file_path(tmpdir: local) -> None:
    download_dir = directory.create_and_get_temporary(tmpdir, "downloads")
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir)
    with Browser(brower_settings) as browser:
        reset_to_not_timed_out(browser)
        browser.open.url(internal_url.DOWNLOAD)
        assert browser.click.download_and_get_file_path(xpath.DownloadPage.DONWLOAD_BUTTON).name == download_page.EXPECTED_FILE_NAME
