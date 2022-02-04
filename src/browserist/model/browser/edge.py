from selenium import webdriver
from .base.driver import BrowserDriver
from .base.type import BrowserType

class EdgeBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.EDGE

    def set_webdriver(self) -> object:
        return webdriver.Edge(
            options = self.edge_options)
      
    def disable_images(self) -> None:
        if self.settings.disable_images:
            pass
    
    def enable_headless(self) -> None:
        if self.settings.headless:
            pass
