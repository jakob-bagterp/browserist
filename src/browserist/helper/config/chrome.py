from selenium.webdriver import ChromeOptions
from ...model.browser import BrowserObject

class ChromeBrowser(BrowserObject):
    def __init__(self):
        self.options: ChromeOptions

    def disable_images(self) -> None:
        if self.settings.disable_images:
            preferences = {"profile.managed_default_content_settings.images": 2, "profile.default_content_settings.images": 2}
            self.options.add_experimental_option("prefs", preferences)
    
    def enable_headless(self) -> None:
        if self.settings.headless:
            self.options.add_argument("headless")
