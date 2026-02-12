import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("width", [1024, 666])
@pytest.mark.xdist_group(name="serial_viewport_tests")
def test_set_viewport_width_non_headless(width: int, browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    _, height = browser.viewport.get.size()
    browser.viewport.set.width(width)
    width_check, height_check = browser.viewport.get.size()
    assert width == width_check
    assert height == height_check
