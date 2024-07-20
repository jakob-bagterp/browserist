import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import external_url, internal_url

from browserist import Browser, helper


@pytest.mark.parametrize("url1, url2", [
    (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_ABOUT),
    (internal_url.MINI_SITE_ABOUT, external_url.EXAMPLE_COM),
    (external_url.EXAMPLE_COM, external_url.IANA_ORG_RESERVED_DOMAINS),
])
def test_open_url_if_not_current(url1: str, url2: str, browser_default_headless: Browser) -> None:
    url1 = helper.url.ensure_trailing_slash(url1)
    url2 = helper.url.ensure_trailing_slash(url2)
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url_if_not_current(url1)
    get_url1 = helper.url.ensure_trailing_slash(browser.get.url.current())
    browser.open.url_if_not_current(url2)
    get_url2 = helper.url.ensure_trailing_slash(browser.get.url.current())
    assert get_url1 == url1
    assert get_url2 == url2
    assert get_url1 != get_url2


@pytest.mark.parametrize("url1, url2, ignore_trailing_slash, expected", [
    (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, True, True),
    (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, False, False),
    (internal_url.MINI_SITE_HOMEPAGE, f"{internal_url.MINI_SITE_HOMEPAGE}/", True, True),
    (internal_url.MINI_SITE_HOMEPAGE, f"{internal_url.MINI_SITE_HOMEPAGE}/", False, False),
])
def test_open_url_if_not_current_ignore_trailing_slash(url1: str, url2: str, ignore_trailing_slash: bool, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url_if_not_current(url1)
    get_url1 = browser.get.url.current()
    browser.open.url_if_not_current(url2, ignore_trailing_slash=ignore_trailing_slash)
    get_url2 = browser.get.url.current()
    assert (get_url1 == get_url2) is expected


@pytest.mark.parametrize("url1, url2, ignore_parameters, expected", [
    (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, True, True),
    (internal_url.MINI_SITE_HOMEPAGE, internal_url.MINI_SITE_HOMEPAGE, False, True),
    (internal_url.MINI_SITE_HOMEPAGE, f"{internal_url.MINI_SITE_HOMEPAGE}?foo=bar", True, True),
    (internal_url.MINI_SITE_HOMEPAGE, f"{internal_url.MINI_SITE_HOMEPAGE}?foo=bar", False, False),
])
def test_open_url_if_not_current_ignore_parameters(url1: str, url2: str, ignore_parameters: bool, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url_if_not_current(url1)
    get_url1 = browser.get.url.current()
    browser.open.url_if_not_current(url2, ignore_parameters=ignore_parameters)
    get_url2 = browser.get.url.current()
    assert (get_url1 == get_url2) is expected


@pytest.mark.parametrize("url1, url2, ignore_https, expected", [
    ("http://example.com", "http://example.com", True, True),
    ("http://example.com", "https://example.com", True, True),
    ("http://example.com", "http://example.com", False, True),
    ("http://example.com", "https://example.com", False, False),
    ("https://example.com", "http://example.com", True, True),
    ("https://example.com", "https://example.com", True, True),
    ("https://example.com", "http://example.com", False, False),
    ("https://example.com", "https://example.com", False, True),
])
def test_open_url_if_not_current_ignore_https(url1: str, url2: str, ignore_https: bool, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url_if_not_current(url1)
    get_url1 = browser.get.url.current()
    browser.open.url_if_not_current(url2, ignore_https=ignore_https)
    get_url2 = browser.get.url.current()
    assert (get_url1 == get_url2) is expected
