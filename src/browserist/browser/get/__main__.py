from selenium.webdriver.remote.webelement import WebElement

from ...model.browser.base.driver import BrowserDriver
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

    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        self.attribute: GetAttributeDriverMethods = GetAttributeDriverMethods(browser_driver)
        self.url: GetUrlDriverMethods = GetUrlDriverMethods(browser_driver)

    def dimensions(self, xpath: str, timeout: float | None = None) -> tuple[int, int]:  # type: ignore
        """Get width and height of element in pixels.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            tuple[int, int]: Width and height in pixels.

        Example:
            ```python title=""
            width, height = browser.get.dimensions("/element/xpath")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_dimensions(self._browser_driver, xpath, timeout)

    def element(self, xpath: str, timeout: float | None = None) -> WebElement:  # type: ignore
        """Get single web element by XPath.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            WebElement: Web element.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_element(self._browser_driver, xpath, timeout)

    def elements(self, xpath: str, timeout: float | None = None) -> list[WebElement]:  # type: ignore
        """Get multiple web elements by XPath.

        Args:
            xpath (str): XPath of the elements.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            list[WebElement]: List of web elements.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_elements(self._browser_driver, xpath, timeout)

    def elements_by_tag(self, tag: str, timeout: float | None = None) -> list[WebElement]:  # type: ignore
        """"Get multiple web elements by HTML tag.

        Args:
            tag (str): HTML tag of the elements. For example, `img` as tag for all `<img>` images, `a` for all `<a>` links, etc.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            list[WebElement]: List of web elements.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_elements_by_tag(self._browser_driver, tag, timeout)

    def page_title(self) -> str:  # type: ignore
        """Get page title of the current page.

        Returns:
            str: Page title.
        """

        if self._timeout_should_continue():
            return get_page_title(self._browser_driver)

    def text(self, xpath: str, timeout: float | None = None) -> str:  # type: ignore
        """Get text from element.

        Note:
            This method assumes that the text field shouldn't be empty and therefore will retry to get the text (for better support of single-page apps with extended loading time).

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            str: Text from element.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_text(self._browser_driver, xpath, timeout)

    def texts(self, xpath: str, timeout: float | None = None) -> list[str]:  # type: ignore
        """Get array of texts from elements. Assumes that the XPath targets multiple elements.

        Args:
            xpath (str): XPath of the elements.
            timeout (float | None, optional): In seconds. Timeout to wait for elements. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            list[str]: List of texts from elements.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_texts(self._browser_driver, xpath, timeout)
