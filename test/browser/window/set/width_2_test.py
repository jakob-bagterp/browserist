import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("width1, width2", [(500, 600), (800, 700)])
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_set_width(width1: int, width2: int, browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.window.set.width(width1)
    get_width1, get_height1 = browser.window.get.size()
    browser.window.set.width(width2)
    get_width2, get_height2 = browser.window.get.size()
    assert width1 == get_width1
    assert width2 == get_width2
    assert get_height1 == get_height2
