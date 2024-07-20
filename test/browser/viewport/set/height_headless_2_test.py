import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("height", [
    600,
    666,
])
def test_set_viewport_height_headless(height: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    width, _ = browser.viewport.get.size()
    browser.viewport.set.height(height)
    width_check, height_check = browser.viewport.get.size()
    assert width == width_check
    assert height == height_check
