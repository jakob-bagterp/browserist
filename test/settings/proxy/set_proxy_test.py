import re

import pytest

from browserist import Browser, BrowserSettings, BrowserType, ProxyProtocol, ProxySettings

PROXY_IP = "72.10.164.178"
PROXY_PORT = 27849
PROXY_TYPE = ProxyProtocol.HTTP
PROXY_URL = f"{PROXY_TYPE.value}://{PROXY_IP}:{PROXY_PORT}"
PROXY_SETTINGS = ProxySettings(
    ip=PROXY_IP,
    port=PROXY_PORT,
    type=PROXY_TYPE,
)

ORIGIN_IP_ADDRESS_PATTERN = re.compile(r'"origin":\s*"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"')  # This is the pattern of the response from httpbin.io/ip, e.g. '"origin": "127.0.0.1:8000"'.


@pytest.mark.parametrize("browser_type, proxy", [
    (BrowserType.CHROME, PROXY_URL),
    (BrowserType.CHROME, PROXY_SETTINGS),
    (BrowserType.EDGE, PROXY_URL),
    (BrowserType.EDGE, PROXY_SETTINGS),
    (BrowserType.FIREFOX, PROXY_SETTINGS),
])
def test_set_proxy(browser_type: BrowserType, proxy: ProxySettings | str) -> None:
    HTTPBIN_IP_CHECK_URL = "https://httpbin.io/ip"

    browser_settings_without_proxy = BrowserSettings(
        type=browser_type,
        headless=True,
        check_connection=True,
    )
    with Browser(browser_settings_without_proxy) as browser_without_proxy:
        browser_without_proxy.open.url(HTTPBIN_IP_CHECK_URL)
        page_source_without_proxy = browser_without_proxy.get.html.page_source()
        assert ORIGIN_IP_ADDRESS_PATTERN.search(page_source_without_proxy)

    browser_settings_with_proxy = BrowserSettings(
        type=browser_type,
        headless=True,
        check_connection=True,
        proxy=proxy,
    )
    with Browser(browser_settings_with_proxy) as browser_with_proxy:
        assert browser_with_proxy._browser_driver.settings._proxy_url == PROXY_URL
        browser_with_proxy.open.url(HTTPBIN_IP_CHECK_URL)
        page_source_with_proxy = browser_with_proxy.get.html.page_source()
        assert ORIGIN_IP_ADDRESS_PATTERN.search(page_source_with_proxy)

    assert page_source_without_proxy != page_source_with_proxy  # Asserting that the IP address should be different when using a proxy.
