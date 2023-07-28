from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .contains_any_text import check_if_contains_any_text
from .contains_text import check_if_contains_text
from .does_exist import check_if_does_exist
from .is_clickable import check_if_is_clickable
from .is_disabled import check_if_is_disabled
from .is_displayed import check_if_is_displayed
from .is_enabled import check_if_is_enabled
from .is_image_loaded import check_if_is_image_loaded
from .is_in_viewport import check_if_is_in_viewport
from .is_selected import check_if_is_selected


class CheckIfDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def contains_any_text(self, xpath: str) -> bool:  # type: ignore
        """Check if element contains any text.

        Args:
            xpath (str): XPath of the element.

        Returns:
            bool: `True` if element contains any text, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_contains_any_text(self._browser_driver, xpath)

    def contains_text(self, xpath: str, regex: str, ignore_case: bool = True) -> bool:  # type: ignore
        """Check if element contains text.

        Args:
            xpath (str): XPath of the element.
            regex (str): Regular expression or text to search for. The condition works for both ordinary text (e.g. `"Submit"`) or regular expression (e.g. `r"colou?r"`). Note it's a search for text, not a strict text match.
            ignore_case (bool, optional): Ignore case when searching for text.

        Returns:
            bool: `True` if element contains text specified in the regex, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_contains_text(self._browser_driver, xpath, regex, ignore_case)

    def does_exist(self, xpath: str) -> bool:  # type: ignore
        """Check if element exists.

        Args:
            xpath (str): XPath of the element.

        Returns:
            bool: `True` if element exists, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_does_exist(self._browser_driver, xpath)

    def is_clickable(self, xpath: str) -> bool:  # type: ignore
        """Check if element is clickable.

        Args:
            xpath (str): XPath of the element.

        Returns:
            bool: `True` if element is clickable, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_is_clickable(self._browser_driver, xpath)

    def is_disabled(self, xpath: str) -> bool:  # type: ignore
        """Check if element is disabled.

        Args:
            xpath (str): XPath of the element.

        Returns:
            bool: `True` if element is disabled, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_is_disabled(self._browser_driver, xpath)

    def is_displayed(self, xpath: str) -> bool:  # type: ignore
        """Check visibility status of an element.

        Args:
            xpath (str): XPath of the element.

        Returns:
            bool: `True` if element is displayed, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_is_displayed(self._browser_driver, xpath)

    def is_enabled(self, xpath: str) -> bool:  # type: ignore
        """Check if element is enabled.

        Args:
            xpath (str): XPath of the element.

        Returns:
            bool: `True` if element is enabled, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_is_enabled(self._browser_driver, xpath)

    def is_image_loaded(self, xpath: str) -> bool:  # type: ignore
        """Check is image is loaded and ready in the DOM.

        Args:
            xpath (str): XPath of the element.

        Returns:
            bool: `True` if image is loaded, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_is_image_loaded(self._browser_driver, xpath)

    def is_in_viewport(self, xpath: str) -> bool:  # type: ignore
        """Check if an element is visible in the current viewport.

        Args:
            xpath (str): XPath of the element.

        Returns:
            bool: `True` if element is visible in the current viewport, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_is_in_viewport(self._browser_driver, xpath)

    def is_selected(self, xpath: str) -> bool:  # type: ignore
        """Check if element is selected, e.g. checkbox or radio button.

        Args:
            xpath (str): XPath of the element.

        Returns:
            bool: `True` if element is selected, `False` otherwise.
        """

        if self._timeout_should_continue():
            return check_if_is_selected(self._browser_driver, xpath)
