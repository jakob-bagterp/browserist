import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, DeviceScreenSize, common_devices


@pytest.mark.parametrize("device", [
    common_devices.Apple.IPHONE_6,
    common_devices.Apple.IPHONE_SE,
    common_devices.Apple.IPAD_AIR_2,
    common_devices.Apple.IPAD_AIR_2,
    common_devices.Apple.IPAD_PRO_9_7_INCH,
])
def test_set_screen_size_by_device_headless(device: DeviceScreenSize, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.viewport.set_size_by_device(device)
    width_check, height_check = browser.viewport.get_size()
    assert device.width == width_check and device.height == height_check
