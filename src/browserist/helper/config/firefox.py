from selenium.webdriver import FirefoxOptions, FirefoxProfile
from ...model.browser import BrowserObject

class FirefoxBrowser(BrowserObject):
    def __init__(self):
        self.options: FirefoxOptions
        self.profile: FirefoxProfile

    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.profile.set_preference('permissions.default.image', 2)
            self.profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    
    def enable_headless(self) -> None:
        if self.settings.headless:
            self.options("--headless")
