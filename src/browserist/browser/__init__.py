__all__ = []

from typing import Union

from ..helper import get
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings

class Browser:
    """Main class of Browserist that sets the Selenium web driver and contains all helper functions."""

    def __init__(self, settings: Union[BrowserSettings, None] = None) -> None:
        """Initiates the browser driver whether the settings calls for Chrome, Firefox, etc."""

        self.browser_driver: BrowserDriver = get.browser_driver(settings)
        self.driver: object = self.browser_driver.webdriver
