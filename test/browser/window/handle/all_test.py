from browserist import Browser


def test_get_all_window_handles(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    assert len(browser.window.handle.all(selenium=True)) == len(browser.window.handle.all(selenium=False)) == 1
    browser.window.open.new_tab()
    assert len(browser.window.handle.all(selenium=True)) == len(browser.window.handle.all(selenium=False)) == 2
    browser.window.open.new()
    assert len(browser.window.handle.all(selenium=True)) == len(browser.window.handle.all(selenium=False)) == 3
