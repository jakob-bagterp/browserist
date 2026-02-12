import pytest

from browserist import helper
from browserist.model.browser.base.settings import BrowserSettings
from browserist.model.browser.base.timeout import TimeoutSettings

TIMED_OUT = True

NOT_TIMED_OUT = not TIMED_OUT


@pytest.mark.parametrize("is_timed_out", [NOT_TIMED_OUT, TIMED_OUT])
def test_helper_set_is_timed_out(is_timed_out: bool) -> None:
    timeout_settings = TimeoutSettings()
    timeout_settings._is_timed_out = is_timed_out
    browser_settings = BrowserSettings(timeout=timeout_settings)
    browser_settings = helper.timeout.set_is_timed_out(browser_settings)
    assert browser_settings.timeout._is_timed_out is True
