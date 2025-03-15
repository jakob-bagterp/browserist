from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.webdriver import WebDriver

from ... import factory
from ...exception.headless import HeadlessModeNotSupportedException
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
        raise HeadlessModeNotSupportedException(self.settings.type)

    def set_download_directory(self) -> None:
        # Safari doesn't support configuration of a default download directory.
        pass

    def set_page_load_strategy(self) -> None:
        self.safari_options = factory.set.page_load_strategy(self, self.safari_options)  # type: ignore

    def disable_default_search_engine_prompt(self) -> None:
        pass

    def set_user_agent(self) -> None:
        if self.settings.user_agent is not None:
            self.safari_options.set_capability("userAgent", self.settings.user_agent)

    def set_service(self) -> SafariService:
        if self.settings._path_to_executable is None:
            return SafariService()
        else:
            return SafariService(executable_path=self.settings._path_to_executable)
