import time

from ..constant import interval, timeout
from ..exception.retry import RetryTimeoutException
from ..model.browser.base.settings import BrowserSettings
from ..model.type.callable import DriverGetBoolCallable, DriverGetTextCallable


def calculate_number_of_retries(total_time: int, interval: int | float) -> int:
    return int(total_time // interval)


def get_text(driver: object, settings: BrowserSettings, input: str, func: DriverGetTextCallable, timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> str:
    text = func(driver, settings, input)
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while not text and retries_left > 0:
        time.sleep(wait_interval_seconds)
        text = func(driver, settings, input)
        retries_left -= 1
        if retries_left == 0:
            raise RetryTimeoutException(func)
    return text


def retry(retries_left: int, wait_interval_seconds: float, func: DriverGetBoolCallable) -> int:
    time.sleep(wait_interval_seconds)
    retries_left -= 1
    if retries_left == 0:
        raise RetryTimeoutException(func)
    return retries_left


def until_condition_is_true(driver: object, settings: BrowserSettings, *args: str | list[object], func: DriverGetBoolCallable, timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> None:
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while func(driver, settings, *args) is False and retries_left > 0:
        retries_left = retry(retries_left, wait_interval_seconds, func)


def until_condition_is_false(driver: object, settings: BrowserSettings, *args: str | list[object], func: DriverGetBoolCallable, timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> None:
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while func(driver, settings, *args) is True and retries_left > 0:
        retries_left = retry(retries_left, wait_interval_seconds, func)


def until_condition_is_false_without_browser_settings(driver: object, *args: str | list[object], func: DriverGetBoolCallable, timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> None:
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while func(driver, *args) is True and retries_left > 0:
        retries_left = retry(retries_left, wait_interval_seconds, func)
