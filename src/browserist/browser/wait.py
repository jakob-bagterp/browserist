import time, random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .check_if_does_element_exist import check_if_does_element_exist
from .wait_for_element import wait_for_element
from .. import helper
from ..constant import timeout
from ..exception.timeout import WaitForUrlTimeoutException
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def wait_until_element_disappears(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    helper.driver.retry_until_condition_is_false(check_if_does_element_exist(driver, xpath), timeout)

def wait_until_url_contains(driver: object, url: str, timeout: int = timeout.LONG) -> None:
    try:
        WebDriverWait(driver, timeout).until(EC.url_contains(url))
    except TimeoutException:
        raise WaitForUrlTimeoutException(driver, url)

def wait_random_time(min_seconds: int = 1, max_seconds: int = timeout.DEFAULT) -> None:
    time.sleep(random.uniform(min_seconds, max_seconds))

class WaitDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def for_element(self, xpath: str) -> None:
        """Wait until element is ready in the DOM and/or on the screen.

        Especially useful for single-page app elements handled/modified by JavaScript, but also standard HTML that doesn't load immediately, this helper function ensures that DOM elements are ready before processing."""

        wait_for_element(self._driver, xpath)

    def until_element_disappears(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until element doesn't exist."""

        wait_until_element_disappears(self._driver, xpath, timeout)

    def until_url_contains(self, url: str, timeout: int = timeout.LONG) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL variable can contain both a fragment (e.g. ?login=true) or a full URL (e.g. https://www.example.com/?login=true)"""

        wait_until_url_contains(self._driver, url, timeout)

    def random_time(self, min_seconds: int = 1, max_seconds: int = 5) -> None:
        """Randomize sleep timing to make actions look less like a bot."""

        wait_random_time(min_seconds, max_seconds)
