from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from ....model.window.controller import WindowHandleController
from ....model.window.tab_or_window import TabOrWindow
from .new_tab_or_window import open_new_tab_or_window


class WindowOpenDriverMethods(DriverMethods):
    __slots__ = ["_controller"]

    def __init__(self, browser_driver: BrowserDriver, controller: WindowHandleController) -> None:
        super().__init__(browser_driver)
        self._controller = controller

    def new_tab(self, url: str | None = None, name: str | None = None, timeout: float | None = None) -> None:
        """Open and switch to new tab in current browser window.

        Args:
            url (str | None, optional): If given, the URL will open in the new tab.
            name (str | None, optional): Unique name to identify the tab so you later can switch back to this tab with the `browser.window.switch_to("some_name")` method.
            timeout (float | None, optional): In seconds. Timeout to wait for the tab. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="4-5"
            from browserist import Browser

            with Browser() as browser:
                browser.window.open.new_tab("https://example.com", "tab_1")
                browser.window.open.new_tab("https://google.com", "tab_2")
                browser.window.switch_to("tab_1")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            open_new_tab_or_window(self._browser_driver, self._controller, TabOrWindow.TAB, timeout, url, name)

    def new_window(self, url: str | None = None, name: str | None = None, timeout: float | None = None) -> None:
        """Open and switch to new browser window.

        Args:
            url (str | None, optional): If given, the URL will open in the new window.
            name (str | None, optional): Unique name to identify the window so you later can switch back to this window with the `browser.window.switch_to("some_name")` method.
            timeout (float | None, optional): In seconds. Timeout to wait for the window. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="4-5"
            from browserist import Browser

            with Browser() as browser:
                browser.window.open.new_window("https://example.com", "window_1")
                browser.window.open.new_window("https://google.com", "window_2")
                browser.window.switch_to("window_1")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            open_new_tab_or_window(self._browser_driver, self._controller, TabOrWindow.WINDOW, timeout, url, name)
