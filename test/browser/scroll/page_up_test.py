from _mock_data.url import internal_url

from browserist import Browser


def test_scroll_page_up(browser_default: Browser) -> None:
    browser = browser_default
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.to_end_of_page()
    _, y_end = browser.scroll.get_position()
    y_screen_height = browser.get.screen.height()
    browser.scroll.page_up()
    _, y_page_up = browser.scroll.get_position()
    assert y_page_up == y_end - y_screen_height - 1
