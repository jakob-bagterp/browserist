from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .does_element_exist import check_if_does_element_exist
from .element_contains_text import check_if_element_contains_text
from .is_element_clickable import check_if_is_element_clickable
from .is_element_disabled import check_if_is_element_disabled
from .is_element_displayed import check_if_is_element_displayed
from .is_element_enabled import check_if_is_element_enabled
from .is_image_element_loaded import check_if_is_image_element_loaded
from .is_image_loaded import check_if_is_image_loaded


class CheckIfDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def element_contains_text(self, xpath: str, regex: str, ignore_case: bool = True, timeout: int = timeout.DEFAULT) -> bool:
        """Check if element contains text. The condition works for both ordinary text (e.g. "Submit") or regular expression (e.g. r"colou?r"). Note it's a search for text, not a strict text match."""

        return check_if_element_contains_text(self._driver, xpath, regex, ignore_case, timeout)

    def does_element_exist(self, xpath: str,) -> bool:
        """Check if element exists."""

        return check_if_does_element_exist(self._driver, xpath)

    def is_element_clickable(self, xpath: str) -> bool:
        """Check if element is clickable."""

        return check_if_is_element_clickable(self._driver, xpath)

    def is_element_enabled(self, xpath: str) -> bool:
        """Check whether element is enabled."""

        return check_if_is_element_enabled(self._driver, xpath)

    def is_element_disabled(self, xpath: str) -> bool:
        """Check whether element is disabled."""

        return check_if_is_element_disabled(self._driver, xpath)

    def is_element_displayed(self, xpath: str) -> bool:
        """Check visibility status of an element."""

        return check_if_is_element_displayed(self._driver, xpath)

    def is_image_element_loaded(self, element: object) -> bool:
        """Check is image element is loaded and ready in the DOM."""

        return check_if_is_image_element_loaded(self._driver, element)

    def is_image_loaded(self, xpath: str, timeout: int = timeout.DEFAULT) -> bool:
        """Check is image is loaded and ready in the DOM."""

        return check_if_is_image_loaded(self._driver, xpath, timeout)
