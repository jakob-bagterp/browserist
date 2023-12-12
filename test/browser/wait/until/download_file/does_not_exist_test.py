from contextlib import nullcontext as does_not_raise
from typing import Any

import _helper
import pytest
from py.path import local

from browserist import Browser, BrowserSettings, helper
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException
from browserist.model.type.path import FilePath


@pytest.mark.parametrize("has_file, expectation", [
    (True, pytest.raises(RetryTimeoutException)),
    (False, does_not_raise()),
])
def test_wait_until_download_file_does_not_exist(has_file: bool, expectation: Any, tmpdir: local) -> None:
    download_dir, file_name, file_path = _helper.file.download_dir_and_file_path_controller(has_file, str(tmpdir))
    assert helper.file.exists(FilePath(file_path)) == has_file
    brower_settings = BrowserSettings(headless=True, download_dir=download_dir)
    with Browser(brower_settings) as browser:
        with expectation:
            _ = browser.wait.until.download_file.does_not_exist(file_name, timeout.VERY_SHORT) is not None
