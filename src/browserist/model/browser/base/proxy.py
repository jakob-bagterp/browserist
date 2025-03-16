from dataclasses import dataclass
from enum import Enum, unique

from .... import helper
from ...type.ip import IPPort, IPv4


@unique
class ProxyProtocol(Enum):
    """Class to define the type of proxy protocol.

    Attributes:
        HTTP: Use HTTP proxy.
        HTTPS: Use HTTPS proxy.
        SOCKS4: Use SOCKS4 proxy.
        SOCKS5: Use SOCKS5 proxy.
    """

    HTTP = "http"
    HTTPS = "https"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"


@dataclass(kw_only=True, slots=True)
class ProxySettings:
    """Class to configure the proxy.

    Args:
        ip (str): IP address of the proxy server. Should be an IPv4 address, e.g. `127.0.0.1`.
        port (int): Port number of the proxy server, e.g. `8080`.
        type (ProxyProtocol, optional): Type of proxy protocol.
        username (str | None, optional): Username for the proxy server.
        password (str | None, optional): Password for the proxy server.
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
