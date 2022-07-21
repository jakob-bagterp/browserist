from _mock_data.url.test_set_2 import URL_TEST_SET_DEFAULT

from browserist import Browser


def test_url_exception_handling_for_open_new_tab_method(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    for test in URL_TEST_SET_DEFAULT.tests:
        with test.expectation:
            _ = browser.window.open.new_tab(test.url) is not None


def test_url_exception_handling_for_open_new_window_method(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    for test in URL_TEST_SET_DEFAULT.tests:
        with test.expectation:
            _ = browser.window.open.new_window(test.url) is not None
