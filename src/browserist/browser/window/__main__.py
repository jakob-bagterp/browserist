from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from ...model.window.controller import WindowHandleController
from .close import window_close
from .fullscreen import window_fullscreen
from .get.__main__ import WindowGetDriverMethods
from .handle.__main__ import WindowHandleDriverMethods
from .maximize import window_maximize
from .minimize import window_minimize
from .open.__main__ import WindowOpenDriverMethods
from .set.__main__ import WindowSetDriverMethods
from .switch_to import switch_to_window


class WindowDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)
        self._controller: WindowHandleController = WindowHandleController(self._driver)
        self.get: WindowGetDriverMethods = WindowGetDriverMethods(browser_driver, settings)
        self.handle: WindowHandleDriverMethods = WindowHandleDriverMethods(browser_driver, settings, self._controller)
        self.open: WindowOpenDriverMethods = WindowOpenDriverMethods(browser_driver, settings, self._controller)
        self.set: WindowSetDriverMethods = WindowSetDriverMethods(browser_driver, settings)

    def close(self) -> None:
        """Close current tab or window."""

        window_close(self._driver, self._controller)

    def fullscreen(self) -> None:
        """Fills the entire screen, similar to pressing F11 in most browsers."""

        window_fullscreen(self._driver)

    def maximize(self) -> None:
        """Enlarges the window. For most operating systems, the window will fill the screen, without blocking the operating system's own menus and toolbars."""

        window_maximize(self._driver)

    def minimize(self) -> None:
        """Minimizes the window of current browsing context. The exact behavior of this command is specific to individual window managers. Minimize Window typically hides the window in the system tray."""

        window_minimize(self._driver)

    def switch_to(self, window_handle: str) -> None:
        """Switch to window/tab by handle ID or name."""

        switch_to_window(self._driver, self._controller, window_handle)

    def switch_to_original_window(self) -> None:
        """Switch to initial window/tab."""

        original_window_handle_id = self._controller.get_handle_id_by_name(self._controller._original_window_name)
        switch_to_window(self._driver, self._controller, original_window_handle_id)
