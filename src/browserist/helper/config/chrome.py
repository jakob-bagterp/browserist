from selenium import webdriver
from ...model.browser import BrowserClass, BrowserType

class ChromeBrowser(BrowserClass):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.CHROME
      
    def disable_images(self) -> None:
        if self.settings.disable_images:
            preferences = {"profile.managed_default_content_settings.images": 2, "profile.default_content_settings.images": 2}
            self.chrome_options.add_experimental_option("prefs", preferences)
    
    def enable_headless(self) -> None:
        if self.settings.headless:
            self.chrome_options.add_argument("headless")

    def set_webdriver(self) -> object:
        return webdriver.Chrome(
            options = self.chrome_options)
