import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("width1, height1, width2, height2", [
    (100, 100, 200, 200),
    (100, 100, 100, 200),
    (100, 100, 200, 100),
])
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_set_size(width1: int, height1: int, width2: int, height2: int, browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.window.set.size(width1, height1)
    get_width1, get_height1 = browser.window.get.size()
    browser.window.set.size(width2, height2)
    get_width2, get_height2 = browser.window.get.size()
    assert get_width1 <= get_width2
    assert get_height1 <= get_height2
