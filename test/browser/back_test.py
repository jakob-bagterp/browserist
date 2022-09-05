from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


def test_go_back(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.EXAMPLE_COM)
    url_1 = browser.get.url.current()
    browser.open.url(internal_url.W3SCHOOLS_COM)
    url_2 = browser.get.url.current()
    browser.back()
    url_back = browser.get.url.current()
    assert url_1 != url_2
    assert url_1 == url_back
