import time, random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ..exception.element import NoElementFoundException
from ..exception.timeout import WaitTimeoutException
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def wait_for_element(driver: object, xpath: str, timeout: int = 5) -> None:
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        raise WaitTimeoutException(driver, xpath)
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath)

def wait_random_time(min_seconds: int = 1, max_seconds: int = 5) -> None:
    time.sleep(random.uniform(min_seconds, max_seconds))

class WaitDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        
    def for_element(self, xpath: str) -> None:
        """Wait until element by XPath is ready in the DOM.

        Especially useful for single-page app elements handled/modified by JavaScript, but also standard HTML that doesn't load immediately, this helper function ensures that DOM elements are ready before processing."""

        wait_for_element(self._driver, xpath)

    def random_time(self, min_seconds: int = 1, max_seconds: int = 5) -> None:
        """Randomize sleep timing to make actions look less like a bot."""

        wait_random_time(min_seconds, max_seconds)
