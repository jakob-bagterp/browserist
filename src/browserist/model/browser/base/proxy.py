from dataclasses import dataclass
from enum import Enum, unique

from ...type.ip import IPv4


@unique
class ProxyProtocol(Enum):
    """Class to define the type of proxy protocol.

    Attributes:
        HTTP: Use HTTP proxy.
        HTTPS: Use HTTPS proxy.
        SOCKS: Use SOCKS proxy.
        SOCKS4: Use SOCKS4 proxy.
        SOCKS5: Use SOCKS5 proxy.
    """

    HTTP = "http"
    HTTPS = "https"
    SOCKS = "socks"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"


@dataclass(kw_only=True, slots=True)
class ProxySettings:
    """Class to configure the proxy.

    Args:
        ip (str): IP address of the proxy server. Should be an IPv4 address, e.g. `127.0.0.1`.
        port (int): Port number of the proxy server, e.g. `8080`.
        username (str | None, optional): Username for the proxy server.
        password (str | None, optional): Password for the proxy server.
        type (ProxyProtocol, optional): Type of proxy protocol.
    """

    ip: str
    port: int
    username: str | None = None
    password: str | None = None
    type: ProxyProtocol = ProxyProtocol.HTTP

    def __post_init__(self) -> None:
        self.ip = IPv4(self.ip)
