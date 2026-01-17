from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .value import get_attribute_value
from .values import get_attribute_values


class GetAttributeDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def value(self, xpath: str, attribute: str, timeout: float | None = None) -> str | None:  # type: ignore
        """Get value from an attribute of an element on the current page.

        Args:
            xpath (str): XPath of the element.
            attribute (str): Attribute name.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            Value of the attribute. If the attribute does not exist, `None` is returned.

        Example:
            Use `src` as attribute to get the source URL from an `<img>` image element.

            ```python title=""
            image_url = browser.get.attribute.value("//xpath/to/img", "src")
            ```

            Use `href` as attribute to get the URL from an `<a>` link element.

            ```python title=""
            link_url = browser.get.attribute.value("//xpath/to/a", "href")
            ```

            Or use other attributes to get the value from a `<meta>` element in the `<head>` section.

            ```python title=""
            meta_content = browser.get.attribute.value("/html/head/meta[1]", "content")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_attribute_value(self._browser_driver, xpath, attribute, timeout)

    def values(self, xpath: str, attribute: str, timeout: float | None = None) -> list[str | None]:  # type: ignore
        """Get values from an attribute of multiple elements on the current page. Assumes that the XPath targets multiple links.

        Args:
            xpath (str): XPath of the elements.
            attribute (str): Attribute name.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            Values of the attribute. If an attribute does not exist, `None` is added to the list.

        Example:
            Use `src` as attribute to get the source URL from `<img>` image elements.

            ```python title=""
            image_urls = browser.get.attribute.values("//img", "src")
            ```

            Use `href` as attribute to get the URL from `<a>` link elements.

            ```python title=""
            link_urls = browser.get.attribute.values("//a", "href")
            ```

            Or use other attributes to get values from `<meta>` elements in the `<head>` section.

            ```python title=""
            meta_contents = browser.get.attribute.values("/html/head/meta", "content")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_attribute_values(self._browser_driver, xpath, attribute, timeout)
