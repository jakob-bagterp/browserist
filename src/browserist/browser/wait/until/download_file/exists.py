from pathlib import Path

from ..... import helper, helper_iteration
from .....model.browser.base.driver import BrowserDriver


def wait_until_file_download_exists(browser_driver: BrowserDriver, file_name: str | Path, timeout: float) -> None:
    file_path = helper.download.get_absolute_file_path(browser_driver, file_name)
    helper_iteration.retry.until_condition_is_true(
        browser_driver, file_path, func=helper.file.exists, timeout=timeout)
