from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


def test_scroll_to_end_of_page(browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    x_default, y_default = browser.scroll.get.position()
    browser.scroll.page.to_end()
    x_end, y_end = browser.scroll.get.position()
    assert x_default == x_end == 0 and y_default < y_end
