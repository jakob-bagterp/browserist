from _config.browser_settings import default

from browserist import Browser


def test_quit() -> None:
    browser = Browser(default.HEADLESS)
    assert browser.driver.service.is_connectable() is True
    browser.quit()
    assert browser.driver.service.is_connectable() is False
