from ....constant import timeout
from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .contains_any_text import wait_until_element_contains_any_text
from .element_disappears import wait_until_element_disappears
from .images_have_loaded import wait_until_images_have_loaded
from .is_clickable import wait_until_element_is_clickable
from .number_of_window_handles_is import wait_until_number_of_window_handles_is
from .page_title.__main__ import WaitUntilPageTitleDriverMethods
from .text.__main__ import WaitUntilTextDriverMethods
from .url.__main__ import WaitUntilUrlDriverMethods


class WaitUntilDriverMethods(DriverMethods):
    __slots__ = ["page_title", "text", "url"]

    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)
        self.page_title: WaitUntilPageTitleDriverMethods = WaitUntilPageTitleDriverMethods(browser_driver, settings)
        self.text: WaitUntilTextDriverMethods = WaitUntilTextDriverMethods(browser_driver, settings)
        self.url: WaitUntilUrlDriverMethods = WaitUntilUrlDriverMethods(browser_driver, settings)

    def contains_any_text(self, xpath: str, timeout: float = timeout.DEFAULT) -> None:
        """Wait until element contains any text (use other method to check for specific text)."""

        wait_until_element_contains_any_text(self._driver, xpath, timeout)

    def element_disappears(self, xpath: str, timeout: float = timeout.DEFAULT) -> None:
        """Wait until element doesn't exist."""

        wait_until_element_disappears(self._driver, xpath, timeout)

    def images_have_loaded(self, xpath: str, timeout: float = timeout.DEFAULT) -> None:
        """Wait until element doesn't exist. The image XPath can target one or more images."""

        wait_until_images_have_loaded(self._driver, xpath, timeout)

    def is_clickable(self, xpath: str, timeout: float = timeout.DEFAULT) -> None:
        """Wait until element is clickable."""

        wait_until_element_is_clickable(self._driver, xpath, timeout)

    def number_of_window_handles_is(self, expected_handles: int, timeout: float = timeout.DEFAULT) -> None:
        """Wait until number of window handles is."""

        wait_until_number_of_window_handles_is(self._driver, expected_handles, timeout)
