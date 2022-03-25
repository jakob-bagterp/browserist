from ....constant import timeout
from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .from_element import get_text_from_element
from .from_multiple_elements import get_text_from_multiple_elements


class GetTextDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def from_element(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get text from element.

        This method assumes that the text field shouldn't be empty and therefore will retry to get the text (for better support of single-page apps with extended loading time)."""

        return get_text_from_element(self._driver, xpath, timeout)

    def from_multiple_elements(self, xpath: str, timeout: int = timeout.DEFAULT) -> list[str]:
        """Get array of texts from elements.

        Assumes that the XPath targets multiple elements."""

        return get_text_from_multiple_elements(self._driver, xpath, timeout)
