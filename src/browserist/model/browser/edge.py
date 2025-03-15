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
        self = factory.chromium.disable_images(self)  # type: ignore

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
        self.edge_options.add_argument(f"--user-agent={self.settings.user_agent}")

    def set_service(self) -> EdgeService:
        if self.settings._path_to_executable is None:
            return EdgeService()
        else:
            return EdgeService(executable_path=self.settings._path_to_executable)
