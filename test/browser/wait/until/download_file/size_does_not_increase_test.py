import os
import time
from contextlib import nullcontext as expectation_of_no_exceptions_raised
from pathlib import Path

import _helper
from _constant import download_page
from _helper import directory
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.download_page import DONWLOAD_BUTTON_XPATH

from browserist import Browser, BrowserSettings
from browserist.constant import idle_timeout

FILE_NAME = "file.txt"


def test_wait_until_download_file_size_does_not_increase_by_timing(tmpdir: Path) -> None:
    """Assume that it's always faster to await a non-existing file (the iteration will break early if no file exists) than an existing, static file that does not increase in size."""

    def get_time_for_wait_until_download_file_size_does_not_increase(browser: Browser) -> float:
        start_time = time.perf_counter_ns()
        browser.wait.until.download_file.size_does_not_increase(FILE_NAME)
        stop_time = time.perf_counter_ns()
        return _helper.time.get_difference(start_time, stop_time)

    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    browser_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with Browser(browser_settings) as browser:
        reset_to_not_timed_out(browser)
        _ = get_time_for_wait_until_download_file_size_does_not_increase(browser)  # Dry run.
        time_without_file = get_time_for_wait_until_download_file_size_does_not_increase(browser)
        file_path = os.path.join(download_dir, FILE_NAME)
        _helper.file.create(file_path)
        assert os.path.exists(file_path) is True
        time_with_file = get_time_for_wait_until_download_file_size_does_not_increase(browser)
        assert time_without_file < time_with_file


def test_wait_until_download_file_size_does_not_increase(tmpdir: Path) -> None:
    download_dir = directory.create_and_get_temporary_download_dir(tmpdir)
    browser_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with expectation_of_no_exceptions_raised():
        with Browser(browser_settings) as browser:
            browser.open.url(internal_url.DOWNLOAD)
            browser.click.button(DONWLOAD_BUTTON_XPATH)
            _ = browser.wait.until.download_file.size_does_not_increase(download_page.EXPECTED_FILE_NAME, idle_timeout.VERY_SHORT) is not None
