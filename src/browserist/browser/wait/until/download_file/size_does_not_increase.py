import time

from browserist.model.type.path import FilePath

from ..... import helper, helper_download
from .....constant import interval
from .....helper.file import exists as file_exists
from .....helper_iteration.retry import calculate_number_of_retries
from .....model.browser.base.driver import BrowserDriver


def wait_until_download_file_size_does_not_increase(
    browser_driver: BrowserDriver, file_name: str, idle_download_timeout: float
) -> None:
    file_path = helper_download.get_file_path(browser_driver, file_name)

    def reset_retries() -> int:
        return calculate_number_of_retries(idle_download_timeout, interval.MEDIUM)

    def get_file_size(file_path: FilePath) -> int:
        return helper.file.get_size(file_path, suppress_file_not_found_error=True)

    def wait_and_then_get_file_size_and_retries_left(previous_retries_left: int) -> tuple[int, int]:
        time.sleep(interval.MEDIUM)
        retries_left = previous_retries_left - 1
        file_size = get_file_size(file_path)
        return file_size, retries_left

    retries_left = reset_retries()
    previous_file_size, retries_left = wait_and_then_get_file_size_and_retries_left(retries_left)
    while retries_left > 0 and file_exists(file_path):
        if get_file_size(file_path) > previous_file_size:
            retries_left = reset_retries()  # As long as the donlowad is active, reset the timeout.
        previous_file_size, retries_left = wait_and_then_get_file_size_and_retries_left(retries_left)
