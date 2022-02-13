__all__ = []

from .check_if import CheckIfDriverMethods
from .click import ClickDriverMethods
from .combo import ComboDriverMethods
from .get.__main__ import GetDriverMethods
from .hover import HoverDriverMethods
from .input import InputDriverMethods
from .open import OpenDriverMethods
from .scroll import ScrollDriverMethods
from .select import SelectDriverMethods
from .tool import ToolDriverMethods
from .wait import WaitDriverMethods
from .. import factory
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.type import BrowserType
from ..model.browser.extension.internet_explorer import InternetExplorerBrowserExtension
from ..model.browser.extension.safari import SafariBrowserExtension

class Browser:
    """Main class of Browserist that sets the Selenium web driver and contains all helper functions."""

    def __init__(self, settings: BrowserSettings | None = None) -> None:
        """Initiates the browser driver whether the settings calls for Chrome, Firefox, etc."""

        if settings is None:
            settings = BrowserSettings() # Use default settings if no custom settings are given.

        self._browser_driver: BrowserDriver = factory.get.browser_driver(settings)
        self.driver: object = self._browser_driver.webdriver

        if self._browser_driver.settings.type is BrowserType.INTERNET_EXPLORER:
            self.ie: InternetExplorerBrowserExtension = InternetExplorerBrowserExtension(self._browser_driver)
        if self._browser_driver.settings.type is BrowserType.SAFARI:
            self.safari: SafariBrowserExtension = SafariBrowserExtension(self._browser_driver)

        self.check_if: CheckIfDriverMethods  = CheckIfDriverMethods(self._browser_driver, settings)
        self.click:    ClickDriverMethods    = ClickDriverMethods(self._browser_driver, settings)
        self.combo:    ComboDriverMethods    = ComboDriverMethods(self._browser_driver, settings)
        self.hover:    HoverDriverMethods    = HoverDriverMethods(self._browser_driver, settings)
        self.get:      GetDriverMethods      = GetDriverMethods(self._browser_driver, settings)
        self.input:    InputDriverMethods    = InputDriverMethods(self._browser_driver, settings)
        self.open:     OpenDriverMethods     = OpenDriverMethods(self._browser_driver, settings)
        self.scroll:   ScrollDriverMethods   = ScrollDriverMethods(self._browser_driver, settings)
        self.select:   SelectDriverMethods   = SelectDriverMethods(self._browser_driver, settings)
        self.tools:    ToolDriverMethods     = ToolDriverMethods(self._browser_driver, settings)
        self.wait:     WaitDriverMethods     = WaitDriverMethods(self._browser_driver, settings)

    def back(self) -> None:
        """Press the browser's back button."""

        self.driver.back()

    def forward(self) -> None:
        """Press the browser's forward button."""

        self.driver.forward()

    def refresh(self) -> None:
        """Refresh the current page."""

        self.driver.refresh()

    def quit(self) -> None:
        """Close the browser."""

        self.driver.quit()
