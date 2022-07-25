from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .attribute.__main__ import GetAttributeDriverMethods
from .dimensions import get_dimensions
from .element import get_element
from .elements import get_elements
from .elements_by_tag import get_elements_by_tag
from .page_title import get_page_title
from .text import get_text
from .texts import get_texts
from .url.__main__ import GetUrlDriverMethods


class GetDriverMethods(DriverMethods):
    __slots__ = ["attribute", "url"]

    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)
        self.attribute: GetAttributeDriverMethods = GetAttributeDriverMethods(browser_driver, settings)
        self.url: GetUrlDriverMethods = GetUrlDriverMethods(browser_driver, settings)

    def dimensions(self, xpath: str, timeout: int | None = None) -> tuple[int, int]:  # type: ignore
        """Get width and height of element in pixels. Usage:

        width, height = browser.get.dimensions("/element/xpath")"""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_dimensions(self._driver, self._settings, xpath, timeout)

    def element(self, xpath: str, timeout: int | None = None) -> object:  # type: ignore
        """Get single web element by XPath."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_element(self._driver, self._settings, xpath, timeout)

    def elements(self, xpath: str, timeout: int | None = None) -> list[object]:  # type: ignore
        """Get multiple web elements by XPath."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_elements(self._driver, self._settings, xpath, timeout)

    def elements_by_tag(self, tag: str, timeout: int | None = None) -> list[object]:  # type: ignore
        """"Get multiple web elements by HTML tag. Examples: "img" as tag for all <img> images, "a" for all <a> links, etc."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_elements_by_tag(self._driver, self._settings, tag, timeout)

    def page_title(self) -> str:  # type: ignore
        """Get page title of the current page."""

        if self._timeout_should_continue():
            return get_page_title(self._driver)

    def text(self, xpath: str, timeout: int | None = None) -> str:  # type: ignore
        """Get text from element.

        This method assumes that the text field shouldn't be empty and therefore will retry to get the text (for better support of single-page apps with extended loading time)."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_text(self._driver, self._settings, xpath, timeout)

    def texts(self, xpath: str, timeout: int | None = None) -> list[str]:  # type: ignore
        """Get array of texts from elements.

        Assumes that the XPath targets multiple elements."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_texts(self._driver, self._settings, xpath, timeout)
