from .get.__main__ import WindowGetDriverMethods
from .set.__main__ import WindowSetDriverMethods
from .fullscreen import window_fullscreen
from .maximize import window_maximize
from .minimize import window_minimize
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods

class WindowDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)
        self.get: WindowGetDriverMethods = WindowGetDriverMethods(browser_driver, settings)
        self.set: WindowSetDriverMethods = WindowSetDriverMethods(browser_driver, settings)

    def fullscreen(self) -> None:
        """Fills the entire screen, similar to pressing F11 in most browsers."""

        window_fullscreen(self._driver)

    def maximize(self) -> None:
        """Enlarges the window. For most operating systems, the window will fill the screen, without blocking the operating system's own menus and toolbars."""

        window_maximize(self._driver)

    def minimize(self) -> None:
        """Minimizes the window of current browsing context. The exact behavior of this command is specific to individual window managers. Minimize Window typically hides the window in the system tray."""

        window_minimize(self._driver)
