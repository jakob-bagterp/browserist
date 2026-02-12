from ..... import helper_download, helper_iteration
from .....helper.file import exists as file_exists
from .....model.browser.base.driver import BrowserDriver


def wait_until_download_file_exists(browser_driver: BrowserDriver, file_name: str, timeout: float) -> None:
    file_path = helper_download.get_file_path(browser_driver, file_name)
    helper_iteration.retry.until_condition_is_true(
        browser_driver, file_path, func=file_exists, timeout=timeout, func_uses_browser_driver=False
    )
