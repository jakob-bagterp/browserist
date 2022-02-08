import time
from typing import Callable
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
