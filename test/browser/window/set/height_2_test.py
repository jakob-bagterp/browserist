import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("height1, height2", [(500, 600), (800, 700)])
@pytest.mark.xdist_group(name="serial_window_tests")
def test_window_set_heigth(height1: int, height2: int, browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.window.set.width(height1)
    get_width1, get_height1 = browser.window.get.size()
    browser.window.set.width(height2)
    get_width2, get_height2 = browser.window.get.size()
    assert height1 == get_height1
    assert height2 == get_height2
    assert get_width1 == get_width2
