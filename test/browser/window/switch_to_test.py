from _config.browser_settings import default
from _mock_data.window_handles import WINDOW_HANDLE_1_NAME, WINDOW_HANDLE_2_NAME

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


def test_switch_to_window_by_name() -> None:
    with Browser(default.HEADLESS) as browser:
        browser.window.open.new(name=WINDOW_HANDLE_2_NAME)
        assert browser.window._controller.count() == 2
        window_handle_2_id = browser.window.handle.current()
        browser.window.switch_to(WINDOW_HANDLE_1_NAME)
        window_handle_1_id = browser.window.handle.current()
        assert window_handle_1_id != window_handle_2_id


def test_switch_to_tab() -> None:
    with Browser(default.HEADLESS) as browser:
        browser.window.open.new_tab()
        browser.window.open.new_tab()

        window_handles = browser.window.handle.all()
        assert len(window_handles) == 3

        for window_handle in window_handles:
            browser.window.switch_to(window_handle)
            assert window_handle == browser.window.handle.current()


def test_switch_to_tab_by_name() -> None:
    with Browser(default.HEADLESS) as browser:
        browser.window.open.new_tab(name=WINDOW_HANDLE_2_NAME)
        assert browser.window._controller.count() == 2
        window_handle_2_id = browser.window.handle.current()
        browser.window.switch_to(WINDOW_HANDLE_1_NAME)
        window_handle_1_id = browser.window.handle.current()
        assert window_handle_1_id != window_handle_2_id
