from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver

from ... import factory
from .base.driver import BrowserDriver
from .base.type import BrowserType


class ChromeBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.CHROME

    def set_webdriver(self) -> WebDriver:
        return WebDriver(
            service=self.chrome_service,
            options=self.chrome_options)

    def disable_images(self) -> None:
        self = factory.chromium.disable_images(self)  # type: ignore

    def enable_headless(self) -> None:
        self = factory.chromium.enable_headless(self)  # type: ignore

    def set_download_directory(self) -> None:
        self = factory.chromium.set_download_directory(self)  # type: ignore

    def set_page_load_strategy(self) -> None:
        self.chrome_options = factory.set.page_load_strategy(self, self.chrome_options)  # type: ignore

    def set_service(self) -> ChromeService:
        if self.settings._path_to_executable is None:
            return ChromeService()
        else:
            return ChromeService(executable_path=self.settings._path_to_executable)
