from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService

from ... import factory
from ...exception.headless import HeadlessNotSupportedException
from .base.driver import BrowserDriver
from .base.type import BrowserType


class SafariBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.SAFARI

    def set_webdriver(self) -> object:
        return webdriver.Safari(
            service=self.safari_service,
            options=self.safari_options)

    def disable_images(self) -> None:
        factory.safari.disable_images(self)

    def enable_headless(self) -> None:
        raise HeadlessNotSupportedException(self.settings.type)

    def set_page_load_strategy(self) -> None:
        self.safari_options = factory.set.page_load_strategy(self, self.safari_options)  # type: ignore

    def set_service(self) -> SafariService:
        if self.settings._path_to_executable is None:
            return SafariService()
        else:
            return SafariService(executable_path=self.settings._path_to_executable)
