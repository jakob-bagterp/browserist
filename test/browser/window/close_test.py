from _config.browser_settings import default

from browserist import Browser


def test_close_window() -> None:
    with Browser(default.HEADLESS) as browser:
        number_of_window_handles_1 = browser.window.handle.count()
        browser.window.open.new()
        number_of_window_handles_2 = browser.window.handle.count()
        browser.window.close()
        number_of_window_handles_3 = browser.window.handle.count()

        assert number_of_window_handles_1 == 1
        assert number_of_window_handles_2 == 2
        assert number_of_window_handles_3 == 1


def test_close_tab() -> None:
    with Browser(default.HEADLESS) as browser:
        number_of_window_handles_1 = browser.window.handle.count()
        browser.window.open.new_tab()
        number_of_window_handles_2 = browser.window.handle.count()
        browser.window.close()
        number_of_window_handles_3 = browser.window.handle.count()

        assert number_of_window_handles_1 == 1
        assert number_of_window_handles_2 == 2
        assert number_of_window_handles_3 == 1
