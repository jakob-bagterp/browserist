import pytest

from browserist import helper
from browserist.constant import timeout
from browserist.model.browser.base.settings import BrowserSettings
from browserist.model.browser.base.timeout.settings import TimeoutSettings
from browserist.model.browser.base.timeout.strategy import TimeoutStrategy

TIMEOUT_SETTINGS = TimeoutSettings(
    strategy=TimeoutStrategy.STOP,
    seconds=timeout.DEFAULT
)

BROWSER_SETTINGS = BrowserSettings(timeout=TIMEOUT_SETTINGS)


@pytest.mark.parametrize("timeout, expected_timeout", [
    (None, TIMEOUT_SETTINGS.seconds),
    (timeout.VERY_SHORT, timeout.VERY_SHORT),
    (2, 2),
])
def test_helper_mediate_timeout(timeout: int | None, expected_timeout: int) -> None:
    assert helper.timeout.mediate_timeout(BROWSER_SETTINGS, timeout) == expected_timeout
