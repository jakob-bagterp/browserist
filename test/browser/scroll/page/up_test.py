from _mock_data.url import internal_url

from browserist import Browser


def test_scroll_page_up(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.page.to_end()
    _, y_end = browser.scroll.get.position()
    y_screen_height = browser.get.screen.height()
    browser.scroll.page.up()
    _, y_page_up = browser.scroll.get.position()
    assert y_page_up == y_end - y_screen_height - 1
