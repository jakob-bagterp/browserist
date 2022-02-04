from selenium import webdriver
from .base.driver import BrowserDriver
from .base.type import BrowserType
from ...helper import chromium

class OperaBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.OPERA

    def set_webdriver(self) -> object:
        return webdriver.Opera(
            options = self.chrome_options)

    def disable_images(self) -> None:
        self = chromium.disable_images(self)
    
    def enable_headless(self) -> None:
        self = chromium.enable_headless(self)
