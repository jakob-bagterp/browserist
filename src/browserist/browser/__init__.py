__all__ = []

from typing import Union
from .. import helper
from ..model.browser import BrowserDriver, BrowserSettings

class Browser:
    def __init__(self, settings: Union[BrowserSettings, None] = None) -> None:
        self.browser_driver: BrowserDriver = helper.get.browser_driver(settings)
        self.driver = self.browser_driver.webdriver
