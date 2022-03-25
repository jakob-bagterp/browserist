from selenium import webdriver

from ... import factory
from ...exception.headless import HeadlessNotSupportedException
from .base.driver import BrowserDriver
from .base.type import BrowserType


class InternetExplorerBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.INTERNET_EXPLORER

    def set_webdriver(self) -> object:
        if self.settings.path_to_executable is None:
            return webdriver.Ie(  # type: ignore
                options=self.ie_options)
        else:
            return webdriver.Ie(  # type: ignore
                executable_path=self.settings.path_to_executable,
                options=self.ie_options)

    def disable_images(self) -> None:
        factory.internet_explorer.disable_images(self)

    def enable_headless(self) -> None:
        raise HeadlessNotSupportedException(self.settings.type)

    def set_page_load_strategy(self) -> None:
        self.ie_options = factory.set.page_load_strategy(self, self.ie_options)  # type: ignore
