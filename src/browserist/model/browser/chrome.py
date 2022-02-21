from selenium import webdriver

from ... import factory
from .base.driver import BrowserDriver
from .base.type import BrowserType


class ChromeBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.CHROME

    def set_webdriver(self) -> object:
        if self.settings.path_to_executable is None:
            return webdriver.Chrome(
                options=self.chrome_options)
        else:
            return webdriver.Chrome(
                executable_path=self.settings.path_to_executable,
                options=self.chrome_options)

    def disable_images(self) -> None:
        self = factory.chromium.disable_images(self)

    def enable_headless(self) -> None:
        self = factory.chromium.enable_headless(self)

    def set_page_load_strategy(self) -> None:
        self.chrome_options = factory.set.page_load_strategy(self, self.chrome_options)
