from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver

from ... import factory
from .base.download.handler import DownloadHandler
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

    def set_download_handler(self) -> DownloadHandler:
        return factory.get.download_handler(self)

    def set_page_load_strategy(self) -> None:
        self.chrome_options = factory.set.page_load_strategy(self, self.chrome_options)  # type: ignore

    def set_service(self) -> ChromeService:
        if self.settings._path_to_executable is None:
            return ChromeService()
        else:
            return ChromeService(executable_path=self.settings._path_to_executable)


class ChromeDownloadHandler(DownloadHandler):
    @property
    def uses_temp_file(self) -> bool:
        return True

    def is_temp_file(self, file_name: str) -> bool:
        return file_name.endswith(".crdownload")
