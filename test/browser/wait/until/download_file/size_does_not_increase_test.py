import os
import time

import _helper
from py.path import local

from browserist import Browser, BrowserSettings
from browserist.constant import timeout

FILE_NAME = "file.txt"


def test_wait_until_download_file_size_does_not_increase_by_timing(tmpdir: local) -> None:
    """Assume that it's faster to await a non-existing file than watch an existing"""

    def get_time_for_wait_until_download_file_size_does_not_increase() -> float:
        start_time = time.perf_counter_ns()
        browser.wait.until.download_file.size_does_not_increase(FILE_NAME, timeout.VERY_SHORT)
        stop_time = time.perf_counter_ns()
        return _helper.time.get_difference(start_time, stop_time)

    download_dir = os.path.join(str(tmpdir), "downloads")
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir)
    with Browser(brower_settings) as browser:
        time_without_file = get_time_for_wait_until_download_file_size_does_not_increase()
        file_path = os.path.join(download_dir, FILE_NAME)
        _helper.file.create(file_path)
        time_with_file = get_time_for_wait_until_download_file_size_does_not_increase()
        assert time_without_file < time_with_file
