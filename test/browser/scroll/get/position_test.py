from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


def test_get_scroll_position(browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    browser.open.url(internal_url.SCROLL_LONG_VERTICAL)
    browser.scroll.page.to_top()
    x_default, y_default = browser.scroll.get.position()
    browser.scroll.page.to_end()
    _, y_end = browser.scroll.get.position()
    assert x_default == 0 and y_default == 0 and y_default < y_end
