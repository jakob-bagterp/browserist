from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .by import scroll_by
from .check_if.__main__ import ScrollCheckIfDriverMethods
from .down_by import scroll_down_by
from .get.__main__ import ScrollGetDriverMethods
from .into_view import scroll_into_view
from .into_view_if_not_visible import scroll_into_view_if_not_visible
from .page.__main__ import ScrollPageDriverMethods
from .to_position import scroll_to_position
from .up_by import scroll_up_by


class ScrollDriverMethods(DriverMethods):
    __slots__ = ["check_if", "get", "page"]

    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)
        self.check_if: ScrollCheckIfDriverMethods = ScrollCheckIfDriverMethods(browser_driver, settings)
        self.get: ScrollGetDriverMethods = ScrollGetDriverMethods(browser_driver, settings)
        self.page: ScrollPageDriverMethods = ScrollPageDriverMethods(browser_driver, settings)

    def by(self, x: int, y: int) -> None:
        """If possible, scroll by X and Y pixels as relative position."""

        scroll_by(self._driver, x, y)

    def down_by(self, pixels: int) -> None:
        """If possible, scroll down in pixels. Horisontal position is unchanged."""

        scroll_down_by(self._driver, pixels)

    def into_view(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Find element and scroll up or down until element is visible."""

        scroll_into_view(self._driver, xpath, timeout)

    def into_view_if_not_visible(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """If not visible, find element and scroll up or down until element is visible."""

        scroll_into_view_if_not_visible(self._driver, xpath, timeout)

    def to_position(self, x: int, y: int) -> None:
        """If possible, scroll to coordinate X and Y pixels of page as absolute position."""

        scroll_to_position(self._driver, x, y)

    def up_by(self, pixels: int) -> None:
        """If possible, scroll up in pixels. Horisontal position is unchanged."""

        scroll_up_by(self._driver, pixels)
