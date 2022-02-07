import time, random
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def wait_random_time(self, min_seconds: int = 1, max_seconds: int = 5) -> None:
    time.sleep(random.uniform(min_seconds, max_seconds))

class WaitDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def random_time(self, min_seconds: int = 1, max_seconds: int = 5) -> None:
        """Randomize sleep timing to make actions look less like a bot."""

        wait_random_time(min_seconds, max_seconds)
