from browserist import Browser


def test_get_all_window_handles(browser_default_headless_scope_function: Browser) -> None:
    browser = browser_default_headless_scope_function
    assert browser.window.handle.count(selenium=True) == browser.window.handle.count(selenium=False) == 1
    browser.window.open.new_tab()
    assert browser.window.handle.count(selenium=True) == browser.window.handle.count(selenium=False) == 2
    browser.window.open.new_window()
    assert browser.window.handle.count(selenium=True) == browser.window.handle.count(selenium=False) == 3
