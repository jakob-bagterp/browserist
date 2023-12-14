from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.ie.webdriver import WebDriver

from ... import factory, helper
from ...exception.headless import HeadlessNotSupportedException
from ..type.path import FilePath
from .base.download.handler import DownloadHandler
from .base.driver import BrowserDriver
from .base.type import BrowserType


class InternetExplorerBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.INTERNET_EXPLORER

    def set_webdriver(self) -> WebDriver:
        return WebDriver(
            service=self.ie_service,
            options=self.ie_options)

    def disable_images(self) -> None:
        factory.internet_explorer.disable_images(self)

    def enable_headless(self) -> None:
        raise HeadlessNotSupportedException(self.settings.type)

    def set_download_directory(self) -> None:
        factory.internet_explorer.set_download_directory(self)

    def set_download_handler(self) -> DownloadHandler:
        return factory.get.download_handler(self)

    def set_page_load_strategy(self) -> None:
        self.ie_options = factory.set.page_load_strategy(self, self.ie_options)  # type: ignore

    def set_service(self) -> IEService:
        if self.settings._path_to_executable is None:
            return IEService()
        else:
            return IEService(executable_path=self.settings._path_to_executable)


class InternetExplorerDownloadHandler(DownloadHandler):
    @property
    def uses_temporary_file(self) -> bool:
        return True

    @property
    def temporary_file_predicts_final_file(self) -> bool:
        return True

        # TODO: To be verified.

    @property
    def temporary_file_extension(self) -> str:
        return ".part"

        # TODO: To be verified.

    def is_temporary_file(self, download_dir: FilePath, file_name: str) -> bool:
        """TODO: To be verified."""

        return file_name.endswith(self.temporary_file_extension) and helper.file.is_file(download_dir, file_name)

        # TODO: To be verified.
