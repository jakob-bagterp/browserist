from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.ie.webdriver import WebDriver

from ... import factory
from ...exception.headless import HeadlessModeNotSupportedException
from ...exception.user_agent import CustomUserAgentNotSupportedException
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
        if self.settings.headless:
            raise HeadlessModeNotSupportedException(self.settings.type)

    def set_download_directory(self) -> None:
        factory.internet_explorer.set_download_directory(self)

    def set_page_load_strategy(self) -> None:
        self.ie_options = factory.set.page_load_strategy(self, self.ie_options)  # type: ignore

    def disable_default_search_engine_prompt(self) -> None:
        pass

    def set_user_agent(self) -> None:
        if self.settings.user_agent is not None:
            raise CustomUserAgentNotSupportedException(self.settings.type)

    def set_service(self) -> IEService:
        if self.settings._path_to_executable is None:
            return IEService()
        else:
            return IEService(executable_path=self.settings._path_to_executable)
