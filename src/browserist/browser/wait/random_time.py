import random
import time


def wait_random_time(min_seconds: int, max_seconds: int) -> None:
    time.sleep(random.uniform(min_seconds, max_seconds))
