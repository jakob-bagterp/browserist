import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser

URL_WITHOUT_HTTPS = "http://httpbin.org/"
URL_WITH_HTTPS = "https://httpbin.org/"


@pytest.mark.parametrize(
    "url1, url2, ignore_https, expected_url",
    [
        (URL_WITHOUT_HTTPS, URL_WITHOUT_HTTPS, True, URL_WITHOUT_HTTPS),
        (URL_WITHOUT_HTTPS, URL_WITH_HTTPS, True, URL_WITHOUT_HTTPS),
        (URL_WITHOUT_HTTPS, URL_WITHOUT_HTTPS, False, URL_WITHOUT_HTTPS),
        (URL_WITHOUT_HTTPS, URL_WITH_HTTPS, False, URL_WITH_HTTPS),
        (URL_WITH_HTTPS, URL_WITHOUT_HTTPS, True, URL_WITH_HTTPS),
        (URL_WITH_HTTPS, URL_WITH_HTTPS, True, URL_WITH_HTTPS),
        (URL_WITH_HTTPS, URL_WITHOUT_HTTPS, False, URL_WITHOUT_HTTPS),
        (URL_WITH_HTTPS, URL_WITH_HTTPS, False, URL_WITH_HTTPS),
    ],
)
def test_open_url_if_not_current_ignore_https(
    url1: str, url2: str, ignore_https: bool, expected_url: str, browser_default_headless: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url1)
    browser.wait.until.url.equals(url1, timeout=20)
    get_url1 = browser.get.url.current()
    assert get_url1 == url1
    browser.open.url_if_not_current(url2, ignore_https=ignore_https)
    get_url2 = browser.get.url.current()
    assert get_url2 == expected_url
