import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.device_screen_size import DEVICE_520_666, DEVICE_666_420
from _mock_data.url import internal_url

from browserist import Browser, DeviceScreenSize


@pytest.mark.parametrize("device", [
    DEVICE_520_666,
    DEVICE_666_420,
])
def test_set_screen_size_by_device_headless(device: DeviceScreenSize, browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.viewport.set_size_by_device(device)
    width_check, height_check = browser.viewport.get_size()
    assert device.width == width_check and device.height == height_check
