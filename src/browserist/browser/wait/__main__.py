from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .for_element import wait_for_element
from .random_time import wait_random_time
from .until_element_disappears import wait_until_element_disappears
from .until_images_have_loaded import wait_until_images_have_loaded
from .until_number_of_window_handles_is import wait_until_number_of_window_handles_is
from .until_page_title_contains import wait_until_page_title_contains
from .until_page_title_is import wait_until_page_title_is
from .until_text_changes import wait_until_text_changes
from .until_text_contains import wait_until_text_contains
from .until_text_is import wait_until_text_is
from .until_url_changes import wait_until_url_changes
from .until_url_contains import wait_until_url_contains
from .until_url_is import wait_until_url_is


class WaitDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def for_element(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until element is ready in the DOM and/or on the screen.

        Especially useful for single-page app elements handled/modified by JavaScript, but also standard HTML that doesn't load immediately, this helper function ensures that DOM elements are ready before processing."""

        wait_for_element(self._driver, xpath, timeout)

    def random_time(self, min_seconds: int = 1, max_seconds: int = 5) -> None:
        """Randomize sleep timing to make actions look less like a bot."""

        wait_random_time(min_seconds, max_seconds)

    def until_element_disappears(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until element doesn't exist."""

        wait_until_element_disappears(self._driver, xpath, timeout)

    def until_images_have_loaded(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until element doesn't exist. The image XPath can target one or more images."""

        wait_until_images_have_loaded(self._driver, xpath, timeout)

    def until_number_of_window_handles_is(self, timeout: int = timeout.DEFAULT) -> None:
        """Wait until number of window handles is."""

        wait_until_number_of_window_handles_is(self._driver, timeout)

    def until_page_title_contains(self, page_title_fragment: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the page title has changed, e.g. after a redirect or update. The input can contain both a fragment or the full page title."""

        wait_until_page_title_contains(self._driver, page_title_fragment, timeout)

    def until_page_title_is(self, page_title: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the page title has changed, e.g. after a redirect or update. The input has to match the exact page title."""

        wait_until_page_title_is(self._driver, page_title, timeout)

    def until_text_changes(self, xpath: str, baseline_text: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the text of an element changes from a baseline text, e.g. after a form action. The text is evaluated as an exact match."""

        wait_until_text_changes(self._driver, xpath, baseline_text, timeout)

    def until_text_contains(self, xpath: str, regex: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the text of an element has changed, e.g. after a form action."""

        wait_until_text_contains(self._driver, xpath, regex, timeout)

    def until_text_is(self, xpath: str, regex: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the text of an element has changed, e.g. after a form action. The text is evaluated as an exact match."""

        wait_until_text_is(self._driver, xpath, regex, timeout)

    def until_url_changes(self, baseline_url: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed from a baseline URL, e.g. after a redirect or form action. The URL is evaluated as an exact match."""

        wait_until_url_changes(self._driver, baseline_url, timeout)

    def until_url_contains(self, url_fragment: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL variable can contain both a fragment (e.g. ?login=true) or a full URL (e.g. https://www.example.com/?login=true)."""

        wait_until_url_contains(self._driver, url_fragment, timeout)

    def until_url_is(self, url: str, timeout: int = timeout.DEFAULT) -> None:
        """Wait until the browser URL has changed, e.g. after a redirect. The URL is evaluated as an exact match."""

        wait_until_url_is(self._driver, url, timeout)
