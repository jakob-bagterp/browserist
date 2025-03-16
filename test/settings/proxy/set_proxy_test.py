import re

from browserist import Browser, BrowserSettings

PROXY_IP = "72.10.164.178"
PROXY_PORT = 27849

ORIGIN_IP_ADDRESS_PATTERN = re.compile(r'"origin":\s*"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"')  # This is the pattern of the response from httpbin.io/ip, e.g. '"origin": "127.0.0.1:8000"'.


def test_set_proxy() -> None:
    browser_settings_without_proxy = BrowserSettings(
        headless=True,
        check_connection=False,
    )
    with Browser(browser_settings_without_proxy) as browser_without_proxy:
        browser_without_proxy.open.url("https://httpbin.io/ip")
        page_source_without_proxy = browser_without_proxy.get.html.page_source()
        assert ORIGIN_IP_ADDRESS_PATTERN.search(page_source_without_proxy)

    proxy_url = f"{PROXY_IP}:{PROXY_PORT}"
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
