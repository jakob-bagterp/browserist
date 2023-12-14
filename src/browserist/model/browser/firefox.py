from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver

from ... import factory
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

    def set_page_load_strategy(self) -> None:
        self.firefox_options = factory.set.page_load_strategy(self, self.firefox_options)  # type: ignore

    def set_service(self) -> FirefoxService:
        if self.settings._path_to_executable is None:
            return FirefoxService()
        else:
            return FirefoxService(executable_path=self.settings._path_to_executable)
