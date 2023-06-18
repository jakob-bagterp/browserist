from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from ... import factory
from .base.driver import BrowserDriver
from .base.type import BrowserType


class OperaBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.OPERA

    def set_webdriver(self) -> object:
        return webdriver.Opera(  # type: ignore
            service=self.chrome_service,
            options=self.chrome_options)

    def disable_images(self) -> None:
        self = factory.chromium.disable_images(self)  # type: ignore

    def enable_headless(self) -> None:
        self = factory.chromium.enable_headless(self)  # type: ignore

    def set_page_load_strategy(self) -> None:
        self.chrome_options = factory.set.page_load_strategy(self, self.chrome_options)  # type: ignore

    def set_service(self) -> ChromeService:
        if self.settings._path_to_executable is None:
            return ChromeService()
        else:
            return ChromeService(executable_path=self.settings._path_to_executable)
