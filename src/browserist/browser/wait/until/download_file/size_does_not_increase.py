from ..... import helper_download, helper_iteration
from .....helper.file import exists as file_exists
from .....helper.file import get_size as get_file_size
from .....model.browser.base.driver import BrowserDriver
from .....model.type.path import FilePath


def wait_until_download_file_size_does_not_increase(browser_driver: BrowserDriver, file_name: str, idle_download_timeout: float) -> None:
    def condition(file_path: FilePath, previous_file_size: int) -> bool:
        return file_exists(file_path) and get_file_size(file_path) > previous_file_size

    file_path = helper_download.get_file_path(browser_driver, file_name)
    file_size = get_file_size(file_path)
    helper_iteration.retry.while_condition_is_true_and_not_timed_out(file_path, file_size, func=condition, idle_timeout=idle_download_timeout)
