import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("width, height", [(1024, 600), (666, 666)])
@pytest.mark.xdist_group(name="serial_viewport_tests")
def test_set_viewport_headless(width: int, height: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.viewport.set.size(width, height)
    width_check, height_check = browser.viewport.get.size()
    assert width == width_check
    assert height == height_check
