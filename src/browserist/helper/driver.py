import time
from typing import Callable
from ..constant import timeout

def retry_and_get_text_from_element(func: Callable[[object, str], str], timeout: int = timeout.DEFAULT, wait_interval_seconds: float = 0.5) -> str:
    text = func
    i = 0
    retries = timeout / wait_interval_seconds
    while len(text) == 0 and i < retries:
        time.sleep(wait_interval_seconds)
        text = func
        i += 1
    return text
