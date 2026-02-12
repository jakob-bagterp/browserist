from contextlib import nullcontext as does_not_raise
from pathlib import Path
from typing import Any

import _helper
import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser, BrowserSettings, helper
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException
from browserist.model.type.path import FilePath


@pytest.mark.parametrize(
    "has_file, expectation", [(True, does_not_raise()), (False, pytest.raises(RetryTimeoutException))]
)
@pytest.mark.xdist_group(name="serial_download_tests")
def test_wait_until_download_file_exists(has_file: bool, expectation: Any, tmpdir: Path) -> None:
    download_dir, file_name, file_path = _helper.file.download_dir_and_file_path_controller(has_file, str(tmpdir))
    assert helper.file.exists(FilePath(file_path)) == has_file
    browser_settings = BrowserSettings(headless=True, download_dir=download_dir, check_connection=False)
    with Browser(browser_settings) as browser:
        reset_to_not_timed_out(browser)
        with expectation:
            _ = browser.wait.until.download_file.exists(file_name, timeout.VERY_SHORT) is not None
