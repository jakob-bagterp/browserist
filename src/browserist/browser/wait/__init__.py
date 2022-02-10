import time, random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .for_element import wait_for_element
from .until_element_disappears import wait_until_element_disappears
from .until_images_have_loaded import wait_until_images_have_loaded
from .until_page_title_contains import wait_until_page_title_contains
from ...constant import timeout
from ...exception.timeout import WaitForPageTitleToChangeTimeoutException, WaitForUrlTimeoutException
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods

def wait_until_page_title_is(driver: object, page_title: str, timeout: int = timeout.DEFAULT) -> None:
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(page_title))
    except TimeoutException:
        raise WaitForPageTitleToChangeTimeoutException(driver, page_title)

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

    def until_images_have_loaded(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until element doesn't exist. The image XPath can target one or more images."""

        wait_until_images_have_loaded(self._driver, xpath, timeout)

    def until_page_title_contains(self, page_title_fragment: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the page title has changed, e.g. after a redirect or update. The input can contain both a fragment or the full page title."""

        wait_until_page_title_contains(self._driver, page_title_fragment, timeout)

    def until_page_title_is(self, page_title: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the page title has changed, e.g. after a redirect or update. The input has to match the exact page title."""

        wait_until_page_title_contains(self._driver, page_title, timeout)

    def until_url_contains(self, url: str, timeout: int = timeout.LONG) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL variable can contain both a fragment (e.g. ?login=true) or a full URL (e.g. https://www.example.com/?login=true)."""

        wait_until_url_contains(self._driver, url, timeout)

    def random_time(self, min_seconds: int = 1, max_seconds: int = 5) -> None:
        """Randomize sleep timing to make actions look less like a bot."""

        wait_random_time(min_seconds, max_seconds)
