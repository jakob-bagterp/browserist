from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.webdriver import WebDriver

from ... import factory
from ...exception.headless import HeadlessNotSupportedException
from .base.download.handler import DownloadHandler
from .base.driver import BrowserDriver
from .base.type import BrowserType


class SafariBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.SAFARI

    def set_webdriver(self) -> WebDriver:
        return WebDriver(
            service=self.safari_service,
            options=self.safari_options)

    def disable_images(self) -> None:
        factory.safari.disable_images(self)

    def enable_headless(self) -> None:
        raise HeadlessNotSupportedException(self.settings.type)

    def set_download_directory(self) -> None:
        # Safari doesn't support configuration of a default download directory.
        pass

    def set_download_handler(self) -> DownloadHandler:
        return factory.get.download_handler(self)

    def set_page_load_strategy(self) -> None:
        self.safari_options = factory.set.page_load_strategy(self, self.safari_options)  # type: ignore

    def set_service(self) -> SafariService:
        if self.settings._path_to_executable is None:
            return SafariService()
        else:
            return SafariService(executable_path=self.settings._path_to_executable)


class SafariDownloadHandler(DownloadHandler):
    @property
    def uses_temporary_file(self) -> bool:
        return True

    @property
    def temporary_file_extension(self) -> str:
        return ".download"

    def is_temporary_file(self, file_name: str) -> bool:
        """When Safari starts a download, it uses `.download` as extension for temporary files.

        For example, it creates the temporary file `file.zip.download` until fully downloaded and then renames it to `file.zip`."""

        return file_name.endswith(f".{self.temporary_file_extension}")
