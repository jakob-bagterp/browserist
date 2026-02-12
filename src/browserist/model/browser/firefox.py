from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver

from ... import factory, helper
from ...exception.proxy import ShouldUseProxySettingsException
from .base.driver import BrowserDriver
from .base.proxy import ProxyProtocol, ProxySettings
from .base.type import BrowserType


class FirefoxBrowserDriver(BrowserDriver):
    def ensure_browser_type(self) -> None:
        self.settings.type = BrowserType.FIREFOX

    def set_webdriver(self) -> WebDriver:
        return WebDriver(service=self.firefox_service, options=self.firefox_options)

    def disable_images(self) -> None:
        if self.settings.disable_images:
            self.firefox_options.set_preference("permissions.default.image", 2)
            self.firefox_options.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")

    def enable_headless(self) -> None:
        if self.settings.headless:
            self.firefox_options.add_argument("--headless")
            self.firefox_options.add_argument("--disable-gpu")

    def set_download_directory(self) -> None:
        if self.settings._download_dir is not None:
            self.firefox_options.set_preference("browser.download.folderList", 2)
            self.firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
            self.firefox_options.set_preference("browser.download.dir", self.settings._download_dir)
            self.firefox_options.set_preference("browser.download.useDownloadDir", True)

    def set_page_load_strategy(self) -> None:
        self.firefox_options = factory.set.page_load_strategy(self, self.firefox_options)  # type: ignore

    def disable_default_search_engine_prompt(self) -> None:
        pass

    def set_user_agent(self) -> None:
        if self.settings.user_agent is not None:
            self.firefox_options.set_preference("general.useragent.override", self.settings.user_agent)

    def set_proxy(self) -> None:
        if self.settings.proxy is not None:
            if not isinstance(self.settings.proxy, ProxySettings):
                raise ShouldUseProxySettingsException(self.settings.type)
            self.firefox_options.set_preference("network.proxy.type", 1)
            proxy_url_partial = helper.proxy.get_url_from_proxy_settings(
                self.settings.proxy, add_protocol=False, add_port=False
            )
            match self.settings.proxy.type:
                case ProxyProtocol.HTTP:
                    self.firefox_options.set_preference("network.proxy.http", proxy_url_partial)
                    self.firefox_options.set_preference("network.proxy.http_port", self.settings.proxy.port)
                case ProxyProtocol.HTTPS:
                    self.firefox_options.set_preference("network.proxy.ssl", proxy_url_partial)
                    self.firefox_options.set_preference("network.proxy.ssl_port", self.settings.proxy.port)
                case ProxyProtocol.SOCKS4 | ProxyProtocol.SOCKS5:
                    self.firefox_options.set_preference("network.proxy.socks", proxy_url_partial)
                    self.firefox_options.set_preference("network.proxy.socks_port", self.settings.proxy.port)
                    self.firefox_options.set_preference("network.proxy.socks_remote_dns", False)

    def set_service(self) -> FirefoxService:
        if self.settings._path_to_executable is None:
            return FirefoxService()
        else:
            return FirefoxService(executable_path=self.settings._path_to_executable)
