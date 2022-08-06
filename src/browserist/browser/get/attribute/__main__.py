from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .value import get_attribute_value
from .values import get_attribute_values


class GetAttributeDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def value(self, xpath: str, attribute: str, timeout: float | None = None) -> str:  # type: ignore
        """Get value from an attribute of an element. Examples:

        Use "src" as attribute to get the source URL from an <img> image tag.

        Use "href" as attribute to get the URL from an <a> link tag."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_attribute_value(self._browser_driver, xpath, attribute, timeout)

    def values(self, xpath: str, attribute: str, timeout: float | None = None) -> list[str]:  # type: ignore
        """Get values from an attribute of multiple elements. Assumes that the XPath targets multiple links. Examples:

        Use "src" as attribute to get the source URL from an <img> image tag.

        Use "href" as attribute to get the URL from an <a> link tag."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_attribute_values(self._browser_driver, xpath, attribute, timeout)
