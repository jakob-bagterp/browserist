from __future__ import annotations

from types import TracebackType

from selenium.webdriver.remote.webdriver import WebDriver

from .. import factory
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.type import BrowserType
from ..model.browser.extension.internet_explorer import InternetExplorerBrowserExtension
from ..model.browser.extension.safari import SafariBrowserExtension
from ..model.viewport.device import DeviceViewportSize
from .check_if.__main__ import CheckIfDriverMethods
from .click.__main__ import ClickDriverMethods
from .combo.__main__ import ComboDriverMethods
from .get.__main__ import GetDriverMethods
from .iframe.__main__ import IframeDriverMethods
from .input.__main__ import InputDriverMethods
from .mouse.__main__ import MouseDriverMethods
from .open.__main__ import OpenDriverMethods
from .prompt.__main__ import PromptDriverMethods
from .screenshot.__main__ import ScreenshotDriverMethods
from .scroll.__main__ import ScrollDriverMethods
from .tool.__main__ import ToolDriverMethods
from .user_agent.__main__ import UserAgentDriverMethods
from .viewport.__main__ import ViewportDriverMethods
from .wait.__main__ import WaitDriverMethods
from .window.__main__ import WindowDriverMethods


class Browser:
    """Main class of Browserist that sets the Selenium web driver and contains all helper functions."""

    __slots__ = [
        "_browser_driver",
        "driver",
        "ie",
        "safari",
        "check_if",
        "click",
        "combo",
        "get",
        "iframe",
        "input",
        "mouse",
        "open",
        "prompt",
        "screenshot",
        "scroll",
        "select",
        "tool",
        "user_agent",
        "viewport",
        "wait",
        "window",
    ]

    def __init__(self, settings: BrowserSettings | None = None) -> None:
        """How to initiate the browser driver:

        Example:
            Basic usage:

            ```python title="Basic usage" linenums="1"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
            ```

            How to initiate the browser driver with [custom settings](../../settings/overview.md) and use Firefox:

            ```python title="" linenums="1" hl_lines="3 5"
            from browserist import Browser, BrowserSettings

            settings = BrowserSettings(browser_type=BrowserType.FIREFOX)

            with Browser(settings) as browser:
                browser.open.url("https://example.com")
            ```
        """

        if settings is None:
            settings = BrowserSettings()  # Use default settings if no custom settings are given.

        self._browser_driver: BrowserDriver = factory.get.browser_driver(settings)
        self.driver: WebDriver = self._browser_driver.get_webdriver()

        self.check_if: CheckIfDriverMethods = CheckIfDriverMethods(self._browser_driver)
        self.click: ClickDriverMethods = ClickDriverMethods(self._browser_driver)
        self.combo: ComboDriverMethods = ComboDriverMethods(self._browser_driver)
        self.get: GetDriverMethods = GetDriverMethods(self._browser_driver)
        self.iframe: IframeDriverMethods = IframeDriverMethods(self._browser_driver)
        self.input: InputDriverMethods = InputDriverMethods(self._browser_driver)
        self.mouse: MouseDriverMethods = MouseDriverMethods(self._browser_driver)
        self.open: OpenDriverMethods = OpenDriverMethods(self._browser_driver)
        self.prompt: PromptDriverMethods = PromptDriverMethods(self._browser_driver)
        self.screenshot: ScreenshotDriverMethods = ScreenshotDriverMethods(self._browser_driver)
        self.scroll: ScrollDriverMethods = ScrollDriverMethods(self._browser_driver)
        self.tool: ToolDriverMethods = ToolDriverMethods(self._browser_driver)
        self.user_agent: UserAgentDriverMethods = UserAgentDriverMethods(self._browser_driver)
        self.viewport: ViewportDriverMethods = ViewportDriverMethods(self._browser_driver)
        self.wait: WaitDriverMethods = WaitDriverMethods(self._browser_driver)
        self.window: WindowDriverMethods = WindowDriverMethods(self._browser_driver)

        match settings.viewport:
            case DeviceViewportSize():
                self.viewport.set.size_by_device(settings.viewport)
            case tuple():
                width, height = settings.viewport
                self.viewport.set.size(width, height)
            case _:
                pass

        match settings.type:
            case BrowserType.INTERNET_EXPLORER:
                self.ie: InternetExplorerBrowserExtension = InternetExplorerBrowserExtension(self._browser_driver)
            case BrowserType.SAFARI:
                self.safari: SafariBrowserExtension = SafariBrowserExtension(self._browser_driver)
            case _:
                pass

    def __enter__(self) -> Browser:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None:
        self.quit()

    def back(self) -> None:
        """Press the browser's back button.

        Example:
            ```python title="" linenums="1" hl_lines="6"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.open.url("https://google.com")
                browser.back()  # Go back to previous page Example.com
            ```
        """

        self.driver.back()

    def forward(self) -> None:
        """Press the browser's forward button.

        Example:
            ```python title="" linenums="1" hl_lines="7"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.open.url("https://google.com")
                browser.back()  # Go back to previous page Example.com
                browser.forward()  # Return to Google.com
            ```
        """

        self.driver.forward()

    def refresh(self) -> None:
        """Refresh the current page.

        Example:
            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.refresh()
            ```
        """

        self.driver.refresh()

    def quit(self) -> None:
        """Quit the browser.

        Example:
            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            browser = Browser()
            browser.open.url("https://example.com")
            browser.quit()
            ```

        Tip:
            Instead of manually quitting the browser with `browser.quit()`, it's recommend to use the [context manager](../../user-guide/context-manager.md) and `with` statements. The example above could then be refactored to:

            ```python linenums="1" hl_lines="3"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
            ```
        """

        self.driver.quit()
