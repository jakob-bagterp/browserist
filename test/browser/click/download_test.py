import os

import pytest
from _constant import download_page
from _helper import directory
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath import xpath
from py.path import local

from browserist import Browser, BrowserSettings
from browserist.constant import idle_timeout


@pytest.mark.parametrize("await_download, expected_file_name", [
    (False, None),
    (False, download_page.EXPECTED_FILE_NAME),
    (True, None),
    (True, download_page.EXPECTED_FILE_NAME),
])
def test_click_download(await_download: bool, expected_file_name: str, tmpdir: local) -> None:
    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    browser_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with Browser(browser_settings) as browser:
        reset_to_not_timed_out(browser)
        browser.open.url(internal_url.DOWNLOAD)
        browser.click.download(
            xpath.DownloadPage.DONWLOAD_BUTTON,
            await_download=await_download,
            expected_file_name=expected_file_name,
            idle_download_timeout=idle_timeout.VERY_SHORT
        )
        if not await_download:
            browser.wait.until.download_file.exists(download_page.EXPECTED_FILE_NAME)
        file_path = os.path.join(download_dir, download_page.EXPECTED_FILE_NAME)
        assert os.path.exists(file_path) is True
        assert os.path.isfile(file_path) is True
