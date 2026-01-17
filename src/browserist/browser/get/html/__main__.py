from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .element_inner import get_element_inner_html
from .element_outer import get_element_outer_html
from .page_source import get_html_page_source


class GetHtmlDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def element_inner(self, xpath: str, timeout: float | None = None) -> str:  # type: ignore
        """Get inner HTML of an element on the current page by XPath.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            Inner HTML of an element.

        Example:
            Get the inner HTML source of an element:

            ```python title="" linenums="1"
            inner_html = browser.get.html.element_inner("//div[@id='content']")
            print(inner_html)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_element_inner_html(self._browser_driver, xpath, timeout)

    def element_outer(self, xpath: str, timeout: float | None = None) -> str:  # type: ignore
        """Get outer HTML of an element on the current page by XPath.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            Outer HTML of an element.

        Example:
            Get the outer HTML source of an element:

            ```python title="" linenums="1"
            outer_html = browser.get.html.element_outer("//div[@id='content']")
            print(outer_html)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_element_outer_html(self._browser_driver, xpath, timeout)

    def page_source(self) -> str:  # type: ignore
        """Get HTML source of the current page.

        Returns:
            HTML page source.

        Example:
            ```python title="" linenums="1"
            page_source = browser.get.html.page_source()
            print(page_source)
            ```
        """

        if self._timeout_should_continue():
            return get_html_page_source(self._browser_driver)
