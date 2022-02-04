from selenium import webdriver
from .base.driver import BrowserDriver
from .base.type import BrowserType

class SafariBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.SAFARI

    def set_webdriver(self) -> object:
        if self.settings.path_to_executable is None:
            return webdriver.Safari()
        else:
            return webdriver.Safari(
                executable_path = self.settings.path_to_executable)

    def disable_images(self) -> None:
        pass

    def enable_headless(self) -> None:
        pass
