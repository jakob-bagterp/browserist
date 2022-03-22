from selenium import webdriver

from ... import factory
from .base.driver import BrowserDriver
from .base.type import BrowserType


class EdgeBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.EDGE

    def set_webdriver(self) -> object:
        if self.settings.path_to_executable is None:
            return webdriver.Edge(  # type: ignore
                options=self.edge_options)
        else:
            return webdriver.Edge(  # type: ignore
                executable_path=self.settings.path_to_executable,
                options=self.edge_options)

    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.edge_options.use_chromium = True  # type: ignore
            preferences = {"profile.managed_default_content_settings.images": 2,
                           "profile.default_content_settings.images": 2}
            self.edge_options.add_experimental_option("prefs", preferences)

    def enable_headless(self) -> None:
        if self.settings.headless:
            self.edge_options.use_chromium = True  # type: ignore
            self.edge_options.add_argument("headless")  # type: ignore
            self.edge_options.add_argument("disable-gpu")  # type: ignore

    def set_page_load_strategy(self) -> None:
        self.edge_options = factory.set.page_load_strategy(self, self.edge_options)  # type: ignore
