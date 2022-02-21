from ....constant import timeout
from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .value import get_attribute_value
from .value_from_multiple_elements import get_attribute_value_from_multiple_elements


class GetAttributeDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def value(self, xpath: str, attribute: str, timeout: int = timeout.DEFAULT) -> str:
        """Get value from an attribute of an element. Examples:

        Use "src" as attribute to get the source URL from an <img> image tag.

        Use "href" as attribute to get the URL from an <a> link tag."""

        return get_attribute_value(self._driver, xpath, attribute, timeout)

    def value_from_multiple_elements(self, xpath: str, attribute: str, timeout: int = timeout.DEFAULT) -> list[str]:
        """Get values from an attribute of multiple elements. Assumes that the XPath targets multiple links. Examples:

        Use "src" as attribute to get the source URL from an <img> image tag.

        Use "href" as attribute to get the URL from an <a> link tag."""

        return get_attribute_value_from_multiple_elements(self._driver, xpath, attribute, timeout)
