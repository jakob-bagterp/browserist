from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


def test_scroll_page_down(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.page.to_top()
    _, y_top = browser.scroll.get.position()
    y_screen_height = browser.screen.height()
    browser.scroll.page.down()
    _, y_page_down = browser.scroll.get.position()
    assert y_page_down == y_top + y_screen_height + 1
