from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver

from ... import factory, helper
from ..type.path import FilePath
from .base.download.handler import DownloadHandler
from .base.driver import BrowserDriver
from .base.type import BrowserType


class FirefoxBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.FIREFOX

    def set_webdriver(self) -> WebDriver:
        return WebDriver(
            service=self.firefox_service,
            options=self.firefox_options)

    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.firefox_options.set_preference("permissions.default.image", 2)
            self.firefox_options.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")

    def enable_headless(self) -> None:
        if self.settings.headless:
            self.firefox_options.add_argument("--headless")  # type: ignore

    def set_download_directory(self) -> None:
        if self.settings._download_dir is not None:
            self.firefox_options.set_preference("browser.download.folderList", 2)
            self.firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
            self.firefox_options.set_preference("browser.download.dir", self.settings._download_dir)
            self.firefox_options.set_preference("browser.download.useDownloadDir", True)

    def set_download_handler(self) -> DownloadHandler:
        return factory.get.download_handler(self)

    def set_page_load_strategy(self) -> None:
        self.firefox_options = factory.set.page_load_strategy(self, self.firefox_options)  # type: ignore

    def set_service(self) -> FirefoxService:
        if self.settings._path_to_executable is None:
            return FirefoxService()
        else:
            return FirefoxService(executable_path=self.settings._path_to_executable)


class FirefoxDownloadHandler(DownloadHandler):
    @property
    def uses_temporary_file(self) -> bool:
        return True

    @property
    def temporary_file_predicts_final_file(self) -> bool:
        return False

    @property
    def temporary_file_extension(self) -> str:
        return ".part"

    def is_temporary_file(self, download_dir: FilePath, file_name: str) -> bool:
        """When Firefox starts a download, it uses `.part` as extension for temporary files.

        For example, it creates the temporary file with a random name `a1b2.zip.part` until fully downloaded and then renames it to `file.zip`."""

        return file_name.endswith(f".{self.temporary_file_extension}") and helper.file.is_file(download_dir, file_name)
