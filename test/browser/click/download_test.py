import os

from _constant import download_page
from _helper import directory
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath import xpath
from py.path import local

from browserist import Browser, BrowserSettings
from browserist.constant import idle_timeout


def test_click_download(tmpdir: local) -> None:
    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir)
    with Browser(brower_settings) as browser:
        reset_to_not_timed_out(browser)
        browser.open.url(internal_url.DOWNLOAD)
        browser.click.download(xpath.DownloadPage.DONWLOAD_BUTTON, idle_download_timeout=idle_timeout.VERY_SHORT)
        browser.wait.until.download_file.exists(download_page.EXPECTED_FILE_NAME)
        file_path = os.path.join(download_dir, download_page.EXPECTED_FILE_NAME)
        assert os.path.exists(file_path) is True
        assert os.path.isfile(file_path) is True
