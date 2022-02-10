import time, random
from ...constant import timeout

def wait_random_time(min_seconds: int = 1, max_seconds: int = timeout.DEFAULT) -> None:
    time.sleep(random.uniform(min_seconds, max_seconds))
