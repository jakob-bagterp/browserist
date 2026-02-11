import os
from pathlib import Path

import pytest
from _constant import download_page
from _helper import directory
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.download_page import DONWLOAD_BUTTON_XPATH

from browserist import Browser, BrowserSettings
from browserist.helper import operating_system


@pytest.mark.skipif(operating_system.is_windows(), reason="This test is not supported on Windows.")
def test_click_download_and_get_file_path(tmpdir: Path) -> None:
    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    browser_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with Browser(browser_settings) as browser:
        reset_to_not_timed_out(browser)
        browser.open.url(internal_url.DOWNLOAD)
        file_path = browser.click.download_and_get_file_path(DONWLOAD_BUTTON_XPATH)
        assert os.path.exists(file_path) is True
        assert os.path.isfile(file_path) is True
        assert file_path.name == download_page.EXPECTED_FILE_NAME
        assert str(file_path.absolute()) == os.path.join(download_dir, download_page.EXPECTED_FILE_NAME)
