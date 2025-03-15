from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.webdriver import WebDriver

from ... import factory
from .base.driver import BrowserDriver
from .base.type import BrowserType


class EdgeBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.EDGE

    def set_webdriver(self) -> WebDriver:
        return WebDriver(
            service=self.edge_service,
            options=self.edge_options)

    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.edge_options.use_chromium = True  # type: ignore
            preferences = {
                "profile.managed_default_content_settings.images": 2,
                "profile.default_content_settings.images": 2
            }
            self.edge_options.add_experimental_option("prefs", preferences)

    def enable_headless(self) -> None:
        if self.settings.headless:
            self.edge_options.use_chromium = True  # type: ignore
            self.edge_options.add_argument("headless")
            self.edge_options.add_argument("disable-gpu")

    def set_download_directory(self) -> None:
        self = factory.chromium.set_download_directory(self)  # type: ignore

    def set_page_load_strategy(self) -> None:
        self.edge_options = factory.set.page_load_strategy(self, self.edge_options)  # type: ignore

    def disable_default_search_engine_prompt(self) -> None:
        pass

    def set_user_agent(self) -> None:
        self = factory.chromium.set_user_agent(self)  # type: ignore

    def set_proxy(self) -> None:
        if self.settings.proxy is not None:
            self.edge_options.add_argument(f"--proxy-server={self.settings.proxy}")

    def set_service(self) -> EdgeService:
        if self.settings._path_to_executable is None:
            return EdgeService()
        else:
            return EdgeService(executable_path=self.settings._path_to_executable)
