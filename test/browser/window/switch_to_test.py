from _config.browser_settings import default

from browserist import Browser


def test_switch_to_window() -> None:
    with Browser(default.HEADLESS) as browser:
        browser.window.open.new()
        browser.window.open.new()

        window_handles = browser.window.handle.all()
        assert len(window_handles) == 3

        for window_handle in window_handles:
            browser.window.switch_to(window_handle)
            assert window_handle == browser.window.handle.current()


def test_switch_to_tab() -> None:
    with Browser(default.HEADLESS) as browser:
        browser.window.open.new_tab()
        browser.window.open.new_tab()

        window_handles = browser.window.handle.all()
        assert len(window_handles) == 3

        for window_handle in window_handles:
            browser.window.switch_to(window_handle)
            assert window_handle == browser.window.handle.current()
