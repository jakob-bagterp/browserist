__all__ = []

from typing import Union
from .check_if_methods import CheckIfDriverMethods
from .click_methods import ClickDriverMethods
from .get_methods import GetDriverMethods
from .open_methods import OpenDriverMethods
from .scroll_methods import ScrollDriverMethods
from .select_methods import SelectDriverMethods
from .validate_methods import ValidateDriverMethods
from .wait_methods import WaitDriverMethods
from .. import helper
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.type import BrowserType
from ..model.extension.internet_explorer import InternetExplorerBrowserExtension
from ..model.extension.safari import SafariBrowserExtension

class Browser:
    """Main class of Browserist that sets the Selenium web driver and contains all helper functions."""

    def __init__(self, settings: Union[BrowserSettings, None] = None) -> None:
        """Initiates the browser driver whether the settings calls for Chrome, Firefox, etc."""

        self._browser_driver: BrowserDriver = helper.get.browser_driver(settings)
        self.driver: object = self._browser_driver.webdriver
        
        match self._browser_driver.settings.type:
            case BrowserType.INTERNET_EXPLORER:
                self.ie: InternetExplorerBrowserExtension = InternetExplorerBrowserExtension(self._browser_driver)
            case BrowserType.SAFARI:
                self.safari: SafariBrowserExtension = SafariBrowserExtension(self._browser_driver)
            case _:
                pass

        self.check_if: CheckIfDriverMethods = CheckIfDriverMethods(self._browser_driver)
        self.click: ClickDriverMethods = ClickDriverMethods(self._browser_driver)
        self.get: GetDriverMethods = GetDriverMethods(self._browser_driver)
        self.open: OpenDriverMethods = OpenDriverMethods(self._browser_driver)
        self.scroll: ScrollDriverMethods = ScrollDriverMethods(self._browser_driver)
        self.select: SelectDriverMethods = SelectDriverMethods(self._browser_driver)
        self.validate: ValidateDriverMethods = ValidateDriverMethods(self._browser_driver)
        self.wait: WaitDriverMethods = WaitDriverMethods(self._browser_driver)

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
        """Close web driver."""

        self.driver.quit()
