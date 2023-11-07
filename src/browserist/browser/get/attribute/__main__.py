from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .value import get_attribute_value
from .values import get_attribute_values


class GetAttributeDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def value(self, xpath: str, attribute: str, timeout: float | None = None) -> str | None:  # type: ignore
        """Get value from an attribute of an element.

        Args:
            xpath (str): XPath of the element.
            attribute (str): Attribute name.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            str | None: Value of the attribute. If the attribute does not exist, `None` is returned.

        Example:
            Use `"src"` as attribute to get the source URL from an `<img>` image tag.

            Use `"href"` as attribute to get the URL from an `<a>` link tag.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_attribute_value(self._browser_driver, xpath, attribute, timeout)

    def values(self, xpath: str, attribute: str, timeout: float | None = None) -> list[str | None]:  # type: ignore
        """Get values from an attribute of multiple elements. Assumes that the XPath targets multiple links.

        Args:
            xpath (str): XPath of the elements.
            attribute (str): Attribute name.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            list[str | None]: Values of the attribute. If an attribute does not exist, `None` is added to the list.

        Example:
            Use `"src"` as attribute to get the source URL from an `<img>` image tag.

            Use `"href"` as attribute to get the URL from an `<a>` link tag.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_attribute_values(self._browser_driver, xpath, attribute, timeout)
