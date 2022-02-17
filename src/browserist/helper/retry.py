import time
from typing import Callable, List
from ..constant import interval, timeout

def get_text_from_element(func: Callable[[object, str], str], timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> str:
    text = str(func)
    retries_left = timeout / wait_interval_seconds
    while not text and retries_left > 0:
        time.sleep(wait_interval_seconds)
        text = str(func)
        retries_left -= 1
    return text

def until_condition_is_true(func: Callable[[object, str | List[object]], bool], timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> None:
    retries_left = timeout / wait_interval_seconds
    while func is False and retries_left > 0:
        time.sleep(wait_interval_seconds)
        retries_left -= 1
        # TODO: Raise exception if it times out/runs out of retries.

def until_condition_is_false(func: Callable[[object, str | List[object]], bool], timeout: int = timeout.DEFAULT, wait_interval_seconds: float = interval.DEFAULT) -> None:
    retries_left = timeout / wait_interval_seconds
    while func is True and retries_left > 0:
        time.sleep(wait_interval_seconds)
        retries_left -= 1
        # TODO: Raise exception if it times out/runs out of retries.
