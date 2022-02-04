from selenium import webdriver
from .base.driver import BrowserDriver
from .base.type import BrowserType
from ...exception.headless import HeadlessNotSupportedException
from ...helper import safari, set

from selenium.webdriver.safari.options import Options

class SafariBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.SAFARI

    def set_webdriver(self) -> object:
        if self.settings.path_to_executable is None:
            return webdriver.Safari(
                options = self.safari_options)
        else:
            return webdriver.Safari(
                executable_path = self.settings.path_to_executable,
                options = self.safari_options)

    def disable_images(self) -> None:
        safari.disable_images(self)

    def enable_headless(self) -> None:
        raise HeadlessNotSupportedException(self.settings.type)

    def set_page_load_strategy(self) -> None:
        self.safari_options = set.page_load_strategy(self, self.safari_options)
