import pytest
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings, DeviceScreenSize


@pytest.mark.parametrize("viewport, expected_width, expected_height", [
    (DeviceScreenSize(666, 420), 666, 420),
    ((375, 667), 375, 667),
    (None, 800, 600),
])
def test_set_screen_size_on_init(viewport: DeviceScreenSize | tuple[int, int] | None, expected_width: int, expected_height: int) -> None:
    settings = BrowserSettings(viewport=viewport, headless=True)
    with Browser(settings) as browser:
        browser.open.url(internal_url.EXAMPLE_COM)
        screen_width, screen_height = browser.viewport.get_size()
        assert screen_width == expected_width and screen_height == expected_height
