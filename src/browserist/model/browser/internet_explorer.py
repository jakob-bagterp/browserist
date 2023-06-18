from selenium import webdriver
from selenium.webdriver.ie.service import Service as IEService

from ... import factory
from ...exception.headless import HeadlessNotSupportedException
from .base.driver import BrowserDriver
from .base.type import BrowserType


class InternetExplorerBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.INTERNET_EXPLORER

    def set_webdriver(self) -> object:
        return webdriver.Ie(
            service=self.ie_service,
            options=self.ie_options)

    def disable_images(self) -> None:
        factory.internet_explorer.disable_images(self)

    def enable_headless(self) -> None:
        raise HeadlessNotSupportedException(self.settings.type)

    def set_page_load_strategy(self) -> None:
        self.ie_options = factory.set.page_load_strategy(self, self.ie_options)  # type: ignore

    def set_service(self) -> IEService:
        if self.settings._path_to_executable is None:
            return IEService()
        else:
            return IEService(executable_path=self.settings._path_to_executable)
