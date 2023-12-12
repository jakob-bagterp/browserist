from contextlib import nullcontext as does_not_raise
from typing import Any

import _helper
import pytest
from py.path import local

from browserist import Browser, BrowserSettings
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


@pytest.mark.parametrize("has_file, expectation", [
    (True, pytest.raises(RetryTimeoutException)),
    (False, does_not_raise()),
])
def test_wait_until_download_file_does_not_exist(has_file: bool, expectation: Any, tmpdir: local) -> None:
    with expectation:
        download_dir, file_path = _helper.file.download_dir_and_file_path_controller(tmpdir, has_file)
        brower_settings = BrowserSettings(headless=True, download_dir=download_dir)
        with Browser(brower_settings) as browser:
            _ = browser.wait.until.download_file.does_not_exist(file_path, timeout.VERY_SHORT) is not None


@pytest.mark.parametrize("has_file, expectation", [
    (True, does_not_raise()),
    (False, pytest.raises(RetryTimeoutException)),
])
def test_wait_until_download_file_exists(has_file: bool, expectation: Any, tmpdir: local) -> None:
    with expectation:
        download_dir, file_path = _helper.file.download_dir_and_file_path_controller(tmpdir, has_file)
        brower_settings = BrowserSettings(headless=True, download_dir=download_dir)
        with Browser(brower_settings) as browser:
            _ = browser.wait.until.download_file.exists(file_path, timeout.VERY_SHORT) is not None
