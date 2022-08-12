import time

from .. import helper
from ..constant import interval, timeout
from ..exception.retry import RetryTimeoutException
from ..helper.timeout import should_continue
from ..model.browser.base.driver import BrowserDriver
from ..model.type.callable import DriverGetBoolCallable, DriverGetTextCallable


def calculate_number_of_retries(total_time: int | float, interval: int | float) -> int:
    return int(total_time // interval)


def get_text(browser_driver: BrowserDriver, input: str, func: DriverGetTextCallable, timeout: float = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> str:
    text = func(browser_driver, input)
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while not text and retries_left > 0:
        time.sleep(wait_interval_seconds)
        text = func(browser_driver, input)
        retries_left -= 1
        if retries_left == 0:
            browser_driver.settings = helper.timeout.set_is_timed_out(browser_driver.settings)
            if not should_continue(browser_driver.settings):
                raise RetryTimeoutException(func)
    return text


def retry_iteration(browser_driver: BrowserDriver, retries_left: int, wait_interval_seconds: float, func: DriverGetBoolCallable) -> int:
    time.sleep(wait_interval_seconds)
    retries_left -= 1
    if retries_left == 0:
        browser_driver.settings = helper.timeout.set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise RetryTimeoutException(func)
    return retries_left


def until_condition_is_true(browser_driver: BrowserDriver, *args: str | list[object], func: DriverGetBoolCallable, timeout: float = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> None:
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while func(browser_driver, *args) is False and retries_left > 0:
        retries_left = retry_iteration(browser_driver, retries_left, wait_interval_seconds, func)


def until_condition_is_false(browser_driver: BrowserDriver, *args: str | list[object], func: DriverGetBoolCallable, timeout: float = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> None:
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while func(browser_driver, *args) is True and retries_left > 0:
        retries_left = retry_iteration(browser_driver, retries_left, wait_interval_seconds, func)
