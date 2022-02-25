import random
import time

from ...constant import timeout


def wait_random_time(min_seconds: int = timeout.VERY_SHORT, max_seconds: int = timeout.DEFAULT) -> None:
    time.sleep(random.uniform(min_seconds, max_seconds))
