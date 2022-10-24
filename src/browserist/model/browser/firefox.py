from selenium import webdriver

from ... import factory
from .base.driver import BrowserDriver
from .base.type import BrowserType


class FirefoxBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.FIREFOX

    def set_webdriver(self) -> object:
        if self.settings._path_to_executable is None:
            return webdriver.Firefox(  # type: ignore
                options=self.firefox_options)
        else:
            return webdriver.Firefox(  # type: ignore
                executable_path=self.settings._path_to_executable,
                options=self.firefox_options)

    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.firefox_options.set_preference("permissions.default.image", 2)
            self.firefox_options.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")

    def enable_headless(self) -> None:
        if self.settings.headless:
            self.firefox_options.add_argument("--headless")  # type: ignore

    def set_page_load_strategy(self) -> None:
        self.firefox_options = factory.set.page_load_strategy(self, self.firefox_options)  # type: ignore
