import pytest
from _helper import external_url, internal_url

from browserist import Browser, helper


@pytest.mark.parametrize("url1, url2", [
    (internal_url.EXAMPLE_COM, internal_url.W3SCHOOLS_COM),
    (internal_url.W3SCHOOLS_COM, external_url.EXAMPLE_COM),
    (external_url.EXAMPLE_COM, external_url.IANA_ORG),
])
def test_open_url_if_not_current(url1: str, url2: str, browser_default_headless: Browser) -> None:
    url1 = helper.url.ensure_trailing_slash(url1)
    url2 = helper.url.ensure_trailing_slash(url2)
    browser = browser_default_headless
    browser.open.url_if_not_current(url1)
    get_url1 = helper.url.ensure_trailing_slash(browser.get.url.current())
    browser.open.url_if_not_current(url2)
    get_url2 = helper.url.ensure_trailing_slash(browser.get.url.current())
    assert get_url1 == url1 and get_url2 == url2 and get_url1 != get_url2


@pytest.mark.parametrize("url1, url2, ignore_trailing_slash, expected", [
    (internal_url.EXAMPLE_COM, internal_url.EXAMPLE_COM, True, True),
    (internal_url.EXAMPLE_COM, internal_url.EXAMPLE_COM, False, False),
    (internal_url.EXAMPLE_COM, f"{internal_url.EXAMPLE_COM}/", True, True),
    (internal_url.EXAMPLE_COM, f"{internal_url.EXAMPLE_COM}/", False, False),
])
def test_open_url_if_not_current_ignore_trailing_slash(url1: str, url2: str, ignore_trailing_slash: bool, expected: bool, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url_if_not_current(url1)
    get_url1 = browser.get.url.current()
    browser.open.url_if_not_current(url2, ignore_trailing_slash=ignore_trailing_slash)
    get_url2 = browser.get.url.current()
    assert (get_url1 == get_url2) is expected

# TODO: Test timing for opening external sites. Should not be run on GitHub Actions
# TODO: Test ignore parameters.
# TODO: Test ignore https.
