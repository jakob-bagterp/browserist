from _mock_data.url import internal_url

from browserist import Browser


def test_scroll_page_down(browser_default: Browser) -> None:
    browser = browser_default
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.to_top_of_page()
    _, y_top = browser.scroll.get_position()
    y_screen_height = browser.get.screen.height()
    browser.scroll.page_down()
    _, y_page_down = browser.scroll.get_position()
    assert y_page_down == y_top + y_screen_height + 1
