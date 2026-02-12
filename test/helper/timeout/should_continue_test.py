import pytest

from browserist import helper
from browserist.model.browser.base.settings import BrowserSettings
from browserist.model.browser.base.timeout import TimeoutSettings, TimeoutStrategy

TIMED_OUT = True

NOT_TIMED_OUT = not TIMED_OUT


@pytest.mark.parametrize(
    "is_timed_out, timeout_strategy, should_continue",
    [
        (NOT_TIMED_OUT, TimeoutStrategy.CONTINUE, True),
        (TIMED_OUT, TimeoutStrategy.CONTINUE, True),
        (NOT_TIMED_OUT, TimeoutStrategy.STOP, True),
        (TIMED_OUT, TimeoutStrategy.STOP, False),
    ],
)
def test_helper_timeout_should_continue(
    is_timed_out: bool, timeout_strategy: TimeoutStrategy, should_continue: bool
) -> None:
    timeout_settings = TimeoutSettings(strategy=timeout_strategy)
    timeout_settings._is_timed_out = is_timed_out
    browser_settings = BrowserSettings(timeout=timeout_settings)
    assert helper.timeout.should_continue(browser_settings) == should_continue
