from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from ....model.window.controller import WindowHandleController
from .all import get_all_window_handles
from .count import count_window_handles
from .current import get_current_window_handle


class WindowHandleDriverMethods(DriverMethods):
    __slots__ = ["_controller"]

    def __init__(self, browser_driver: BrowserDriver, controller: WindowHandleController) -> None:
        super().__init__(browser_driver)
        self._controller = controller

    def all(self, selenium: bool = False) -> list[str]:  # type: ignore
        """Get list of IDs of all open tabs or windows.

        Args:
            selenium (bool, optional): Set to `True` if you want the Selenium handle IDs rather than from Browserist's internal window handle controller.

        Returns:
            List of IDs of all open tabs or windows.

        Example:
            ```python title=""
            window_handles = browser.window.handle.all()
            ```
        """

        if self._timeout_should_continue():
            return get_all_window_handles(self._browser_driver, self._controller, selenium)

    def count(self, selenium: bool = False) -> int:  # type: ignore
        """Count number of open tabs or windows.

        Args:
            selenium (bool, optional): Set to `True` if you want the Selenium handle IDs rather than from Browserist's internal window handle controller.

        Returns:
            Number of open tabs or windows.

        Example:
            ```python title=""
            sum_of_window_handles = browser.window.handle.count()
            ```
        """

        if self._timeout_should_continue():
            return count_window_handles(self._browser_driver, self._controller, selenium)

    def current(self) -> str:  # type: ignore
        """Get the ID of the current tab or window.

        Returns:
            ID of the current tab or window. e.g. `CDwindow-69663F4BF867CC38F6AF46D55BFC1A8A`.

        Example:
            ```python title=""
            current_window_handle = browser.window.handle.current()
            ```
        """

        if self._timeout_should_continue():
            return get_current_window_handle(self._browser_driver)
