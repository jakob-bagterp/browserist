from __future__ import annotations

from types import TracebackType

from .. import factory
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.type import BrowserType
from ..model.browser.extension.internet_explorer import InternetExplorerBrowserExtension
from ..model.browser.extension.safari import SafariBrowserExtension
from .check_if.__main__ import CheckIfDriverMethods
from .click.__main__ import ClickDriverMethods
from .combo.__main__ import ComboDriverMethods
from .get.__main__ import GetDriverMethods
from .iframe.__main__ import IframeDriverMethods
from .input.__main__ import InputDriverMethods
from .mouse.__main__ import MouseDriverMethods
from .open.__main__ import OpenDriverMethods
from .scroll.__main__ import ScrollDriverMethods
from .select.__main__ import SelectDriverMethods
from .tool.__main__ import ToolDriverMethods
from .wait.__main__ import WaitDriverMethods
from .window.__main__ import WindowDriverMethods


class Browser:
    """Main class of Browserist that sets the Selenium web driver and contains all helper functions."""

    def __init__(self, settings: BrowserSettings | None = None) -> None:
        """Initiates the browser driver whether the settings calls for Chrome, Firefox, etc."""

        if settings is None:
            settings = BrowserSettings()  # Use default settings if no custom settings are given.

        self._browser_driver: BrowserDriver = factory.get.browser_driver(settings)
        self.driver: object = self._browser_driver.webdriver

        if self._browser_driver.settings.type is BrowserType.INTERNET_EXPLORER:
            self.ie: InternetExplorerBrowserExtension = InternetExplorerBrowserExtension(self._browser_driver)
        if self._browser_driver.settings.type is BrowserType.SAFARI:
            self.safari: SafariBrowserExtension = SafariBrowserExtension(self._browser_driver)

        self.check_if: CheckIfDriverMethods = CheckIfDriverMethods(self._browser_driver, settings)
        self.click: ClickDriverMethods = ClickDriverMethods(self._browser_driver, settings)
        self.combo: ComboDriverMethods = ComboDriverMethods(self._browser_driver, settings)
        self.get: GetDriverMethods = GetDriverMethods(self._browser_driver, settings)
        self.iframe: IframeDriverMethods = IframeDriverMethods(self._browser_driver, settings)
        self.input: InputDriverMethods = InputDriverMethods(self._browser_driver, settings)
        self.mouse: MouseDriverMethods = MouseDriverMethods(self._browser_driver, settings)
        self.open: OpenDriverMethods = OpenDriverMethods(self._browser_driver, settings)
        self.scroll: ScrollDriverMethods = ScrollDriverMethods(self._browser_driver, settings)
        self.select: SelectDriverMethods = SelectDriverMethods(self._browser_driver, settings)
        self.tool: ToolDriverMethods = ToolDriverMethods(self._browser_driver, settings)
        self.wait: WaitDriverMethods = WaitDriverMethods(self._browser_driver, settings)
        self.window: WindowDriverMethods = WindowDriverMethods(self._browser_driver, settings)

    def __enter__(self) -> Browser:
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        self.quit()

    def back(self) -> None:
        """Press the browser's back button."""

        self.driver.back()  # type: ignore

    def forward(self) -> None:
        """Press the browser's forward button."""

        self.driver.forward()  # type: ignore

    def refresh(self) -> None:
        """Refresh the current page."""

        self.driver.refresh()  # type: ignore

    def quit(self) -> None:
        """Quit the browser."""

        self.driver.quit()  # type: ignore
