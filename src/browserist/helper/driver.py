import time
from typing import Callable, List, Union
from ..constant import timeout

def retry_and_get_text_from_element(func: Callable[[object, str], str], timeout: int = timeout.DEFAULT, wait_interval_seconds: float = 0.5) -> str:
    text = str(func)
    i = 0
    retries = timeout / wait_interval_seconds
    while not text and i < retries:
        time.sleep(wait_interval_seconds)
        text = str(func)
        i += 1
    return text

def retry_until_condition_is_true(func: Callable[[object, Union[str, List[object]]], bool], timeout: int = timeout.DEFAULT, wait_interval_seconds: float = 0.5) -> None:
    i = 0
    retries = timeout / wait_interval_seconds
    while func is False and i < retries:
        time.sleep(wait_interval_seconds)
        i += 1

def retry_until_condition_is_false(func: Callable[[object, Union[str, List[object]]], bool], timeout: int = timeout.DEFAULT, wait_interval_seconds: float = 0.5) -> None:
    i = 0
    retries = timeout / wait_interval_seconds
    while func is True and i < retries:
        time.sleep(wait_interval_seconds)
        i += 1
