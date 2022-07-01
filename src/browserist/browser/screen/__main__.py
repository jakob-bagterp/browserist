from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .height import get_screen_height
from .size import get_screen_size
from .width import get_screen_width


class ScreenSizeDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def height(self) -> int:
        """Get inner height of the screen in pixels."""

        return get_screen_height(self._driver)

    def size(self) -> tuple[int, int]:
        """Get inner width and height of the screen in pixels. Usage:

        width, height = browser.screen.size()"""

        return get_screen_size(self._driver)

    def width(self) -> int:
        """Get inner width of the screen in pixels."""

        return get_screen_width(self._driver)
