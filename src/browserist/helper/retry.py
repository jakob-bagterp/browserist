import time
from ..constant import interval, timeout
from ..model.callable import DriverGetBoolCallable, DriverGetTextCallable

def calculate_number_of_retries(total_time: int, interval: int | float) -> int:
    return int(total_time // interval)

def get_text_from_element(func: DriverGetTextCallable, timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> str:
    text = str(func)
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while not text and retries_left > 0:
        time.sleep(wait_interval_seconds)
        text = str(func)
        retries_left -= 1
    return text

def until_condition_is_true(func: DriverGetBoolCallable, timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> None:
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while func is False and retries_left > 0:
        time.sleep(wait_interval_seconds)
        retries_left -= 1
        # TODO: Raise exception if it times out/runs out of retries.

def until_condition_is_false(func: DriverGetBoolCallable, timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> None:
    retries_left = calculate_number_of_retries(timeout, wait_interval_seconds)
    while func is True and retries_left > 0:
        time.sleep(wait_interval_seconds)
        retries_left -= 1
        # TODO: Raise exception if it times out/runs out of retries.
