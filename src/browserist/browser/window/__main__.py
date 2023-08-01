from ...model.browser.base.driver import BrowserDriver
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
    __slots__ = ["_controller", "get", "handle", "open", "set"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        self._controller: WindowHandleController = WindowHandleController(self._browser_driver)
        self.get: WindowGetDriverMethods = WindowGetDriverMethods(browser_driver)
        self.handle: WindowHandleDriverMethods = WindowHandleDriverMethods(browser_driver, self._controller)
        self.open: WindowOpenDriverMethods = WindowOpenDriverMethods(browser_driver, self._controller)
        self.set: WindowSetDriverMethods = WindowSetDriverMethods(browser_driver)

    def close(self) -> None:
        """Close current tab or window."""

        if self._timeout_should_continue():
            window_close(self._browser_driver, self._controller)

    def fullscreen(self) -> None:
        """Fills the entire screen. Similar to pressing F11 in most browsers."""

        if self._timeout_should_continue():
            window_fullscreen(self._browser_driver)

    def maximize(self) -> None:
        """Enlarge the browser window to maximum allowed size.

        Note:
            For most operating systems, the window will fill the screen, without blocking the operating system's own menus and toolbars. Obviously, the size of the browser window also depends on the device and its screen resolution.
        """

        if self._timeout_should_continue():
            window_maximize(self._browser_driver)

    def minimize(self) -> None:
        """Minimizes the window of current browsing context.

        Note:
            The exact behavior of this command is specific to individual window managers. Minimize Window typically hides the window in the system tray.
        """

        if self._timeout_should_continue():
            window_minimize(self._browser_driver)

    def switch_to(self, window_handle: str) -> None:
        """Switch to window/tab by handle ID or name.

        Args:
            window_handle (str): Handle ID or name of window/tab to switch to.

        Example:
            ```python title="" linenums="1"
            from browserist import Browser

            with Browser() as browser:
                browser.window.open.new_tab("https://example.com", "tab_1")
                browser.window.open.new_tab("https://www.google.com", "tab_2")
                browser.window.switch_to("tab_1")
            ```
        """

        if self._timeout_should_continue():
            switch_to_window(self._browser_driver, self._controller, window_handle)

    def switch_to_original_window(self) -> None:
        """Switch to initial window/tab.

        Note:
            Browserist automatically remembers the handle ID of the initial window/tab when the browser is first opened.
        """

        if self._timeout_should_continue():
            original_window_handle_id = self._controller.get_handle_id_by_name(self._controller._original_window_name)
            switch_to_window(self._browser_driver, self._controller, original_window_handle_id)
