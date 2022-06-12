from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .contains_text import check_if_contains_text
from .does_exist import check_if_does_exist
from .is_clickable import check_if_is_clickable
from .is_disabled import check_if_is_disabled
from .is_displayed import check_if_is_displayed
from .is_enabled import check_if_is_enabled
from .is_image_loaded import check_if_is_image_loaded


class CheckIfDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def contains_text(self, xpath: str, regex: str, ignore_case: bool = True, timeout: int = timeout.DEFAULT) -> bool:
        """Check if element contains text. The condition works for both ordinary text (e.g. "Submit") or regular expression (e.g. r"colou?r"). Note it's a search for text, not a strict text match."""

        return check_if_contains_text(self._driver, xpath, regex, ignore_case, timeout)

    def does_exist(self, xpath: str,) -> bool:
        """Check if element exists."""

        return check_if_does_exist(self._driver, xpath)

    def is_clickable(self, xpath: str) -> bool:
        """Check if element is clickable."""

        return check_if_is_clickable(self._driver, xpath)

    def is_disabled(self, xpath: str) -> bool:
        """Check whether element is disabled."""

        return check_if_is_disabled(self._driver, xpath)

    def is_displayed(self, xpath: str) -> bool:
        """Check visibility status of an element."""

        return check_if_is_displayed(self._driver, xpath)

    def is_enabled(self, xpath: str) -> bool:
        """Check whether element is enabled."""

        return check_if_is_enabled(self._driver, xpath)

    def is_image_loaded(self, xpath: str, timeout: int = timeout.DEFAULT) -> bool:
        """Check is image is loaded and ready in the DOM."""

        return check_if_is_image_loaded(self._driver, xpath, timeout)
