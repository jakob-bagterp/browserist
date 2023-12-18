import os
import time
from contextlib import nullcontext as expectation_of_no_exceptions_raised

import _helper
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from py.path import local

from browserist import Browser, BrowserSettings
from browserist.constant import idle_timeout

FILE_NAME = "file.txt"


def test_wait_until_download_file_size_does_not_increase_by_timing(tmpdir: local) -> None:
    """Assume that it's faster to await a non-existing file than an existing, static file that does not increase in size."""

    def get_time_for_wait_until_download_file_size_does_not_increase(browser: Browser) -> float:
        start_time = time.perf_counter_ns()
        browser.wait.until.download_file.size_does_not_increase(FILE_NAME)
        stop_time = time.perf_counter_ns()
        return _helper.time.get_difference(start_time, stop_time)

    download_dir = os.path.join(str(tmpdir), "downloads")
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir)
    with Browser(brower_settings) as browser:
        reset_to_not_timed_out(browser)
        _ = get_time_for_wait_until_download_file_size_does_not_increase(browser)  # Dry run.
        time_without_file = get_time_for_wait_until_download_file_size_does_not_increase(browser)
        file_path = os.path.join(download_dir, FILE_NAME)
        _helper.file.create(file_path)
        assert os.path.exists(file_path) is True
        time_with_file = get_time_for_wait_until_download_file_size_does_not_increase(browser)
        assert time_without_file < time_with_file


def test_wait_until_download_file_size_does_not_increase(tmpdir: local) -> None:
    download_dir = os.path.join(str(tmpdir), "downloads")
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir)
    with expectation_of_no_exceptions_raised():
        with Browser(brower_settings) as browser:
            browser.open.url(internal_url.DOWNLOAD)
            browser.click.button("//button[@id='download']")
            _ = browser.wait.until.download_file.size_does_not_increase("file.zip", idle_timeout.VERY_SHORT) is not None
