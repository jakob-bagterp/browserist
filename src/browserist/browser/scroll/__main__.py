from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .by import scroll_by
from .check_if.__main__ import ScrollCheckIfDriverMethods
from .down_by import scroll_down_by
from .get.__main__ import ScrollGetDriverMethods
from .into_view import scroll_into_view
from .into_view_if_not_visible import scroll_into_view_if_not_in_viewport
from .left_by import scroll_left_by
from .page.__main__ import ScrollPageDriverMethods
from .right_by import scroll_right_by
from .to_position import scroll_to_position
from .up_by import scroll_up_by


class ScrollDriverMethods(DriverMethods):
    __slots__ = ["check_if", "get", "page"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        self.check_if: ScrollCheckIfDriverMethods = ScrollCheckIfDriverMethods(browser_driver)
        self.get: ScrollGetDriverMethods = ScrollGetDriverMethods(browser_driver)
        self.page: ScrollPageDriverMethods = ScrollPageDriverMethods(browser_driver)

    def by(self, x: int, y: int, delay_seconds: float = 1) -> None:
        """If possible, scroll by X and Y pixels as relative position. Add custom delay in seconds to ensure the view is updated after scroll."""

        if self._timeout_should_continue():
            scroll_by(self._browser_driver, x, y, delay_seconds)

    def down_by(self, pixels: int, delay_seconds: float = 1) -> None:
        """If possible, scroll down in pixels. Horisontal position is unchanged. Add custom delay in seconds to ensure the view is updated after scroll."""

        if self._timeout_should_continue():
            scroll_down_by(self._browser_driver, pixels, delay_seconds)

    def into_view(self, xpath: str, timeout: float | None = None, delay_seconds: float = 1) -> None:
        """Find element and scroll up or down until element is visible. Add custom delay in seconds to ensure the view is updated after scroll."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            scroll_into_view(self._browser_driver, xpath, timeout, delay_seconds)

    def into_view_if_not_in_viewport(self, xpath: str, timeout: float | None = None, delay_seconds: float = 1) -> None:
        """If not visible in the current viewport, find element and scroll up or down until element is visible. Add custom delay in seconds to ensure the view is updated after scroll."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            scroll_into_view_if_not_in_viewport(self._browser_driver, xpath, timeout, delay_seconds)

    def left_by(self, pixels: int, delay_seconds: float = 1) -> None:
        """If possible, scroll left in pixels. Horisontal position is unchanged. Add custom delay in seconds to ensure the view is updated after scroll."""

        if self._timeout_should_continue():
            scroll_left_by(self._browser_driver, pixels, delay_seconds)

    def right_by(self, pixels: int, delay_seconds: float = 1) -> None:
        """If possible, scroll right in pixels. Horisontal position is unchanged. Add custom delay in seconds to ensure the view is updated after scroll."""

        if self._timeout_should_continue():
            scroll_right_by(self._browser_driver, pixels, delay_seconds)

    def to_position(self, x: int, y: int, delay_seconds: float = 1) -> None:
        """If possible, scroll to coordinate X and Y pixels of page as absolute position. Add custom delay in seconds to ensure the view is updated after scroll."""

        if self._timeout_should_continue():
            scroll_to_position(self._browser_driver, x, y, delay_seconds)

    def up_by(self, pixels: int, delay_seconds: float = 1) -> None:
        """If possible, scroll up in pixels. Horisontal position is unchanged. Add custom delay in seconds to ensure the view is updated after scroll."""

        if self._timeout_should_continue():
            scroll_up_by(self._browser_driver, pixels, delay_seconds)
