from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


def test_scroll_to_end_of_page(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.SCROLL_LONG_VERTICAL)
    browser.scroll.page.to_top()
    x_default, y_default = browser.scroll.get.position()
    assert x_default == 0
    assert y_default == 0
    total_srcroll_height = browser.scroll.get.total_height()
    assert total_srcroll_height > 0
    browser.scroll.page.to_end()
    x_end, y_end = browser.scroll.get.position()
    assert x_end == 0
    assert y_end > y_default
