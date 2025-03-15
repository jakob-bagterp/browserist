import re

import pytest

from browserist import Browser, BrowserSettings

ORIGIN_IP_ADDRESS_PATTERN = re.compile(r'"origin":\s*"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"')  # This is the pattern of the response from httpbin.io/ip, e.g. '"origin": "127.0.0.1:8000"'.


@pytest.mark.parametrize("proxy_ip, proxy_port", [
    ("72.10.164.178", 27849),
])
def test_set_proxy(proxy_ip: str, proxy_port: int) -> None:
    browser_settings_without_proxy = BrowserSettings(
        headless=True,
        check_connection=False,
    )
    with Browser(browser_settings_without_proxy) as browser_without_proxy:
        browser_without_proxy.open.url("https://httpbin.io/ip")
        page_source_without_proxy = browser_without_proxy.get.html.page_source()
        assert ORIGIN_IP_ADDRESS_PATTERN.search(page_source_without_proxy)

    proxy_url = f"{proxy_ip}:{proxy_port}"
    browser_settings_with_proxy = BrowserSettings(
        headless=True,
        check_connection=False,
        proxy=proxy_url,
    )
    with Browser(browser_settings_with_proxy) as browser_with_proxy:
        browser_with_proxy.open.url("https://httpbin.io/ip")
        page_source_with_proxy = browser_with_proxy.get.html.page_source()
        assert ORIGIN_IP_ADDRESS_PATTERN.search(page_source_with_proxy)

    assert page_source_without_proxy != page_source_with_proxy  # Asserting that the IP address should be different when using a proxy.
