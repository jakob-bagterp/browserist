__all__ = []

from typing import Union
from .check_if import CheckIfDriverMethods
from .click import ClickDriverMethods
from .combo import ComboDriverMethods
from .get import GetDriverMethods
from .input import InputDriverMethods
from .open import OpenDriverMethods
from .scroll import ScrollDriverMethods
from .select import SelectDriverMethods
from .tools import ToolsDriverMethods
from .validate import ValidateDriverMethods
from .wait import WaitDriverMethods
from .. import helper
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.type import BrowserType
from ..model.browser.extension.internet_explorer import InternetExplorerBrowserExtension
from ..model.browser.extension.safari import SafariBrowserExtension

class Browser:
    """Main class of Browserist that sets the Selenium web driver and contains all helper functions."""

    def __init__(self, settings: Union[BrowserSettings, None] = None) -> None:
        """Initiates the browser driver whether the settings calls for Chrome, Firefox, etc."""

        self._browser_driver: BrowserDriver = helper.get.browser_driver(settings)
        self.driver: object = self._browser_driver.webdriver

        if self._browser_driver.settings.type is BrowserType.INTERNET_EXPLORER:
            self.ie: InternetExplorerBrowserExtension = InternetExplorerBrowserExtension(self._browser_driver)
        if self._browser_driver.settings.type is BrowserType.SAFARI:
            self.safari: SafariBrowserExtension = SafariBrowserExtension(self._browser_driver)

        self.check_if: CheckIfDriverMethods  = CheckIfDriverMethods(self._browser_driver)
        self.click:    ClickDriverMethods    = ClickDriverMethods(self._browser_driver)
        self.combo:    ComboDriverMethods    = ComboDriverMethods(self._browser_driver)
        self.get:      GetDriverMethods      = GetDriverMethods(self._browser_driver)
        self.input:    InputDriverMethods    = InputDriverMethods(self._browser_driver)
        self.open:     OpenDriverMethods     = OpenDriverMethods(self._browser_driver)
        self.scroll:   ScrollDriverMethods   = ScrollDriverMethods(self._browser_driver)
        self.select:   SelectDriverMethods   = SelectDriverMethods(self._browser_driver)
        self.tools:    ToolsDriverMethods    = ToolsDriverMethods(self._browser_driver)
        self.validate: ValidateDriverMethods = ValidateDriverMethods(self._browser_driver)
        self.wait:     WaitDriverMethods     = WaitDriverMethods(self._browser_driver)

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
