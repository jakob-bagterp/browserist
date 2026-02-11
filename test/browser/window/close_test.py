import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser


@pytest.mark.xdist_group(name="serial_window_tests")
def test_close_window(browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    number_of_window_handles_1 = browser.window.handle.count(selenium=True)
    browser.window.open.new_window()
    number_of_window_handles_2 = browser.window.handle.count(selenium=True)
    browser.window.close()
    number_of_window_handles_3 = browser.window.handle.count(selenium=True)

    assert number_of_window_handles_1 == 1
    assert number_of_window_handles_2 == 2
    assert number_of_window_handles_3 == 1


@pytest.mark.xdist_group(name="serial_window_tests")
def test_close_tab(browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    number_of_window_handles_1 = browser.window.handle.count(selenium=True)
    browser.window.open.new_tab()
    number_of_window_handles_2 = browser.window.handle.count(selenium=True)
    browser.window.close()
    number_of_window_handles_3 = browser.window.handle.count(selenium=True)

    assert number_of_window_handles_1 == 1
    assert number_of_window_handles_2 == 2
    assert number_of_window_handles_3 == 1
