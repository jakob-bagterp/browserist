from selenium import webdriver
from .base.driver import BrowserDriver
from .base.type import BrowserType
from ...helper import chromium

class ChromeBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.CHROME

    def set_webdriver(self) -> object:
        return webdriver.Chrome(
            options = self.chrome_options)
      
    def disable_images(self) -> None:
        self = chromium.disable_images(self)

    def enable_headless(self) -> None:
        self = chromium.enable_headless(self)
