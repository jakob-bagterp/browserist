from selenium import webdriver
from ...model.browser import BrowserClass

class FirefoxBrowser(BrowserClass):
    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.firefox_profile.set_preference("permissions.default.image", 2)
            self.firefox_profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")
    
    def enable_headless(self) -> None:
        if self.settings.headless:
            self.firefox_options("--headless")
