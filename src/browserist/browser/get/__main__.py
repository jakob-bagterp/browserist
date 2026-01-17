from selenium.webdriver.remote.webelement import WebElement

from browserist.browser.get.meta_description import get_meta_description

from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .attribute.__main__ import GetAttributeDriverMethods
from .dimensions import get_dimensions
from .element import get_element
from .elements import get_elements
from .elements_by_tag import get_elements_by_tag
from .html.__main__ import GetHtmlDriverMethods
from .page_title import get_page_title
from .text import get_text
from .texts import get_texts
from .url.__main__ import GetUrlDriverMethods


class GetDriverMethods(DriverMethods):
    __slots__ = ["attribute", "html", "url"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        self.attribute: GetAttributeDriverMethods = GetAttributeDriverMethods(browser_driver)
        self.html: GetHtmlDriverMethods = GetHtmlDriverMethods(browser_driver)
        self.url: GetUrlDriverMethods = GetUrlDriverMethods(browser_driver)

    def dimensions(self, xpath: str, timeout: float | None = None) -> tuple[int, int]:  # type: ignore
        """Get width and height of element in pixels.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            Width and height in pixels.

        Example:
            ```python title=""
            width, height = browser.get.dimensions("//xpath/to/element")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_dimensions(self._browser_driver, xpath, timeout)

    def element(self, xpath: str, timeout: float | None = None) -> WebElement:  # type: ignore
        """Get single `WebElement` by XPath.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            Web element.

        Example:
            ```python title="" linenums="1"
            element = browser.get.element("//xpath/to/element")
            print(element.text)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_element(self._browser_driver, xpath, timeout)

    def elements(self, xpath: str, timeout: float | None = None) -> list[WebElement]:  # type: ignore
        """Get multiple `WebElement`s by XPath. Assumes that the XPath targets multiple elements.

        Args:
            xpath (str): XPath of the elements.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            List of web elements of type `WebElement`.

        Example:
            ```python title="" linenums="1"
            elements = browser.get.elements("//xpath/to/elements")
            for element in elements:
                print(element.text)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_elements(self._browser_driver, xpath, timeout)

    def elements_by_tag(self, tag: str, timeout: float | None = None) -> list[WebElement]:  # type: ignore
        """"Get multiple `WebElement`s by HTML tag. Assumes that the XPath targets multiple elements.

        Args:
            tag (str): HTML tag of the elements. For example, `img` as tag for all `<img>` images, `a` for all `<a>` links, etc.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            List of web elements of type `WebElement`.

        Example:
            Get and print all paragraphs of a web page:

            ```python title="" linenums="1"
            elements = browser.get.elements_by_tag("p")
            for element in elements:
                print(element.text)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_elements_by_tag(self._browser_driver, tag, timeout)

    def meta_description(self) -> str:   # type: ignore
        """Get meta description of the current page.

        Returns:
            The meta description content of the current page. If no meta description is found, an empty string is returned.

        Example:
            ```python title="" linenums="1"
            meta_description = browser.get.meta_description()
            print(meta_description)
            ```
        """

        if self._timeout_should_continue():
            return get_meta_description(self._browser_driver)

    def page_title(self) -> str:  # type: ignore
        """Get page title of the current page.

        Returns:
            Page title.

        Example:
            ```python title="" linenums="1"
            page_title = browser.get.page_title()
            print(page_title)
            ```
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
            Text from element.

        Example:
            ```python title="" linenums="1"
            element_text = browser.get.text("//xpath/to/element")
            print(element_text)
            ```
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
            List of texts from elements.

        Example:
            ```python title="" linenums="1"
            element_texts = browser.get.texts("//xpath/to/elements")
            for element_text in element_texts:
                print(element_text)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_texts(self._browser_driver, xpath, timeout)
