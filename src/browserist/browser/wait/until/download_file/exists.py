from pathlib import Path

from ..... import helper, helper_download, helper_iteration
from .....model.browser.base.driver import BrowserDriver
from .....model.type.path import FilePath


def wait_until_download_file_exists(browser_driver: BrowserDriver, file_name: str | Path, timeout: float) -> None:
    def file_exists(browser_driver: BrowserDriver, file_path: FilePath) -> bool:
        return helper.file.exists(file_path)

    file_path = helper_download.get_absolute_file_path(browser_driver, file_name)
    helper_iteration.retry.until_condition_is_true(
        browser_driver, file_path, func=file_exists, timeout=timeout)
