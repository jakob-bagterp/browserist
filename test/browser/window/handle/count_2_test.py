import pytest
from _helper.timeout import reset_to_not_timed_out

from browserist import Browser


@pytest.mark.xdist_group(name="serial_window_tests")
def test_get_all_window_handles(browser_default_headless_scope_function: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_scope_function)
    assert browser.window.handle.count(selenium=True) == browser.window.handle.count(selenium=False) == 1
    browser.window.open.new_tab()
    assert browser.window.handle.count(selenium=True) == browser.window.handle.count(selenium=False) == 2
    browser.window.open.new_window()
    assert browser.window.handle.count(selenium=True) == browser.window.handle.count(selenium=False) == 3
