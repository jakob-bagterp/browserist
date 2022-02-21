from selenium import webdriver

from ... import factory
from .base.driver import BrowserDriver
from .base.type import BrowserType


class FirefoxBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.FIREFOX

    def set_webdriver(self) -> object:
        if self.settings.path_to_executable is None:
            return webdriver.Firefox(
                firefox_profile=self.firefox_profile,
                options=self.firefox_options)
        else:
            return webdriver.Firefox(
                executable_path=self.settings.path_to_executable,
                firefox_profile=self.firefox_profile,
                options=self.firefox_options)

    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.firefox_profile.set_preference("permissions.default.image", 2)
            self.firefox_profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")

    def enable_headless(self) -> None:
        if self.settings.headless:
            self.firefox_options.add_argument("--headless")

    def set_page_load_strategy(self) -> None:
        self.firefox_options = factory.set.page_load_strategy(self, self.firefox_options)
