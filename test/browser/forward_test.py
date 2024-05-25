from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


def test_go_forward(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    url_1 = browser.get.url.current()
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    url_2 = browser.get.url.current()
    browser.back()
    url_back = browser.get.url.current()
    browser.forward()
    url_forward = browser.get.url.current()
    assert url_1 != url_2
    assert url_1 == url_back
    assert url_2 == url_forward
