from copy import deepcopy

import pytest

from browserist.helper.proxy import get_url_from_proxy_settings
from browserist.model.browser.base.proxy import ProxyProtocol, ProxySettings

VALID_PROXY_SETTINGS_HTTP = ProxySettings(
    ip="255.255.255.255",
    port=8080,
    type=ProxyProtocol.HTTP,
)

VALID_PROXY_SETTINGS_HTTPS = deepcopy(VALID_PROXY_SETTINGS_HTTP)
VALID_PROXY_SETTINGS_HTTPS.type = ProxyProtocol.HTTPS

VALID_PROXY_SETTINGS_SOCKS4 = deepcopy(VALID_PROXY_SETTINGS_HTTP)
VALID_PROXY_SETTINGS_SOCKS4.type = ProxyProtocol.SOCKS4

VALID_PROXY_SETTINGS_SOCKS5 = deepcopy(VALID_PROXY_SETTINGS_HTTP)
VALID_PROXY_SETTINGS_SOCKS5.type = ProxyProtocol.SOCKS5


@pytest.mark.parametrize("proxy_settings, add_protocol, add_port, expected", [
    (VALID_PROXY_SETTINGS_HTTP, True, True, "http://255.255.255.255:8080"),
    (VALID_PROXY_SETTINGS_HTTP, True, False, "http://255.255.255.255"),
    (VALID_PROXY_SETTINGS_HTTP, False, True, "255.255.255.255:8080"),
    (VALID_PROXY_SETTINGS_HTTP, False, False, "255.255.255.255"),
    (VALID_PROXY_SETTINGS_HTTPS, True, True, "https://255.255.255.255:8080"),
    (VALID_PROXY_SETTINGS_HTTPS, True, False, "https://255.255.255.255"),
    (VALID_PROXY_SETTINGS_HTTPS, False, True, "255.255.255.255:8080"),
    (VALID_PROXY_SETTINGS_HTTPS, False, False, "255.255.255.255"),
    (VALID_PROXY_SETTINGS_SOCKS4, True, True, "socks4://255.255.255.255:8080"),
    (VALID_PROXY_SETTINGS_SOCKS4, True, False, "socks4://255.255.255.255"),
    (VALID_PROXY_SETTINGS_SOCKS4, False, True, "255.255.255.255:8080"),
    (VALID_PROXY_SETTINGS_SOCKS4, False, False, "255.255.255.255"),
    (VALID_PROXY_SETTINGS_SOCKS5, True, True, "socks5://255.255.255.255:8080"),
    (VALID_PROXY_SETTINGS_SOCKS5, True, False, "socks5://255.255.255.255"),
    (VALID_PROXY_SETTINGS_SOCKS5, False, True, "255.255.255.255:8080"),
    (VALID_PROXY_SETTINGS_SOCKS5, False, False, "255.255.255.255"),
])
def test_helper_get_url_from_proxy_settings(proxy_settings: ProxySettings, add_protocol: bool, add_port: bool, expected: str) -> None:
    assert get_url_from_proxy_settings(proxy_settings, add_protocol, add_port) == expected
