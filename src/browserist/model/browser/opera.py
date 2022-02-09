from selenium import webdriver
from .base.driver import BrowserDriver
from .base.type import BrowserType
from ...helper import browser_factory

class OperaBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.OPERA

    def set_webdriver(self) -> object:
        if self.settings.path_to_executable is None:
            return webdriver.Opera(
                options = self.chrome_options)
        else:
            return webdriver.Opera(
                executable_path = self.settings.path_to_executable,
                options = self.chrome_options)

    def disable_images(self) -> None:
        self = browser_factory.chromium.disable_images(self)

    def enable_headless(self) -> None:
        self = browser_factory.chromium.enable_headless(self)

    def set_page_load_strategy(self) -> None:
        self.chrome_options = browser_factory.set.page_load_strategy(self, self.chrome_options)
