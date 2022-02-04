from selenium import webdriver
from .base.driver import BrowserDriver
from .base.type import BrowserType
from ...exception.headless import HeadlessNotSupportedException

class InternetExplorerBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.INTERNET_EXPLORER

    def set_webdriver(self) -> object:
        if self.settings.path_to_executable is None:
            return webdriver.Ie(
                options = self.ie_options)
        else:
            return webdriver.Ie(
                executable_path = self.settings.path_to_executable,
                options = self.ie_options)

    def disable_images(self) -> None:
        pass

    def enable_headless(self) -> None:
        raise HeadlessNotSupportedException(self.settings.type)
