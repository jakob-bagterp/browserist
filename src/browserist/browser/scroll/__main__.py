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
        """If possible, scroll by X and Y pixels as relative to current position.

        Args:
            x (int): In pixels. Scroll on horisontal X axis as relative to current position. Can be positive or negative.
            y (int): In pixels. Scroll on vertical Y axis as relative to current position. Can be positive or negative.
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.by(0, 100)
            ```
        """

        if self._timeout_should_continue():
            scroll_by(self._browser_driver, x, y, delay_seconds)

    def down_by(self, pixels: int, delay_seconds: float = 1) -> None:
        """If possible, scroll down by Y pixels on the current page. Horisontal position is unchanged.

        Args:
            pixels (int): Amount to scroll down as relative to current position.
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.down_by(100)
            ```
        """

        if self._timeout_should_continue():
            scroll_down_by(self._browser_driver, pixels, delay_seconds)

    def into_view(self, xpath: str, timeout: float | None = None, delay_seconds: float = 1) -> None:
        """Find element on the current page and scroll up or down until element is visible.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.into_view("//xpath/to/element")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            scroll_into_view(self._browser_driver, xpath, timeout, delay_seconds)

    def into_view_if_not_in_viewport(self, xpath: str, timeout: float | None = None, delay_seconds: float = 1) -> None:
        """If not visible in the current viewport, find element and scroll up or down until element is visible.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.into_view_if_not_in_viewport("//xpath/to/element")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            scroll_into_view_if_not_in_viewport(self._browser_driver, xpath, timeout, delay_seconds)

    def left_by(self, pixels: int, delay_seconds: float = 1) -> None:
        """If possible, scroll left by X pixels. Horisontal position is unchanged.

        Args:
            pixels (int): Amount to scroll left as relative to current position.
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.left_by(50)
            ```
        """

        if self._timeout_should_continue():
            scroll_left_by(self._browser_driver, pixels, delay_seconds)

    def right_by(self, pixels: int, delay_seconds: float = 1) -> None:
        """If possible, scroll right by X pixels. Horisontal position is unchanged.

        Args:
            pixels (int): Amount to scroll right as relative to current position.
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.right_by(50)
            ```
        """

        if self._timeout_should_continue():
            scroll_right_by(self._browser_driver, pixels, delay_seconds)

    def to_position(self, x: int, y: int, delay_seconds: float = 1) -> None:
        """If possible, scroll to coordinate X and Y pixels of page as absolute position.

        Args:
            x (int): Absolute position in pixels on horisontal X axis.
            y (int): Absolute position in pixels on vertical Y axis.
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.to_position(0, 100)
            ```
        """

        if self._timeout_should_continue():
            scroll_to_position(self._browser_driver, x, y, delay_seconds)

    def up_by(self, pixels: int, delay_seconds: float = 1) -> None:
        """If possible, scroll up by Y pixels. Horisontal position is unchanged.

        Args:
            pixels (int): Amount to scroll up as relative to current position.
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.up_by(50)
            ```
        """

        if self._timeout_should_continue():
            scroll_up_by(self._browser_driver, pixels, delay_seconds)
