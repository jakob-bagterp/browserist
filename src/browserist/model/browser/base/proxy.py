from dataclasses import dataclass
from enum import Enum, unique

from .... import helper
from ...type.ip import IPPort, IPv4


@unique
class ProxyProtocol(Enum):
    """Class to define the type of proxy protocol as used in [`ProxySettings`](proxy-settings.md).

    Attributes:
        ProxyProtocol.HTTP (Enum): Use HTTP proxy.
        ProxyProtocol.HTTPS (Enum): Use HTTPS proxy.
        ProxyProtocol.SOCKS4 (Enum): Use SOCKS4 proxy.
        ProxyProtocol.SOCKS5 (Enum): Use SOCKS5 proxy.

    Example:
        How to set a different proxy protocol than the default `HTTP`:

        ```python title="" linenums="1" hl_lines="6"
        from browserist import Browser, BrowserSettings, ProxySettings, ProxyProtocol

        proxy_settings = ProxySettings(
            ip="127.0.0.1",
            port=8080,
            protocol=ProxyProtocol.HTTPS)

        settings = BrowserSettings(proxy=proxy_settings)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    HTTP = "http"
    HTTPS = "https"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"


@dataclass(kw_only=True, slots=True)
class ProxySettings:
    """Class to configure the proxy as used in [`BrowserSettings`](browser-settings.md).

    Args:
        ip (str): IP address of the proxy server. Should be an IPv4 address, e.g. `127.0.0.1`.
        port (int): Port number of the proxy server, e.g. `8080`.
        type (ProxyProtocol, optional): Type of proxy protocol.
        username (str | None, optional): Username for the proxy server.
        password (str | None, optional): Password for the proxy server.

    Example:
        How to set a proxy server with a basic URL:

        ```python title="" linenums="1" hl_lines="3-5"
        from browserist import Browser, BrowserSettings, ProxySettings

        proxy_settings = ProxySettings(
            ip="127.0.0.1",
            port=8080)

        settings = BrowserSettings(proxy=proxy_settings)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    ip: str
    port: int
    type: ProxyProtocol = ProxyProtocol.HTTP
    username: str | None = None
    password: str | None = None

    def __post_init__(self) -> None:
        self.ip = IPv4(self.ip)
        self.port = IPPort(self.port)

    def get_url(self) -> str:
        """Returns a proxy server URL based on the settings."""

        return helper.proxy.get_url_from_proxy_settings(self)
