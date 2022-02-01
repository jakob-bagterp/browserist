from selenium import webdriver
from . import BrowserDriver
from .type import BrowserType

class FirefoxBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.FIREFOX

    def set_webdriver(self) -> object:
        return webdriver.Firefox(
            firefox_profile = self.firefox_profile,
            options = self.firefox_options)

    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.firefox_profile.set_preference("permissions.default.image", 2)
            self.firefox_profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")
    
    def enable_headless(self) -> None:
        if self.settings.headless:
            self.firefox_options("--headless")
