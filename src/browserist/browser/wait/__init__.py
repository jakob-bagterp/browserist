from .for_element import wait_for_element
from .random_time import wait_random_time
from .until_element_disappears import wait_until_element_disappears
from .until_images_have_loaded import wait_until_images_have_loaded
from .until_page_title_contains import wait_until_page_title_contains
from .until_page_title_is import wait_until_page_title_is
from .until_url_contains import wait_until_url_contains
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods

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

        wait_until_page_title_is(self._driver, page_title, timeout)

    def until_url_contains(self, url: str, timeout: int = timeout.LONG) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL variable can contain both a fragment (e.g. ?login=true) or a full URL (e.g. https://www.example.com/?login=true)."""

        wait_until_url_contains(self._driver, url, timeout)

    def random_time(self, min_seconds: int = 1, max_seconds: int = 5) -> None:
        """Randomize sleep timing to make actions look less like a bot."""

        wait_random_time(min_seconds, max_seconds)
