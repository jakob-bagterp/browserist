import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.device_viewport import DEVICE_520_666, DEVICE_666_420
from _mock_data.url import internal_url

from browserist import Browser, DeviceViewportSize


@pytest.mark.parametrize("device", [
    DEVICE_520_666,
    DEVICE_666_420,
])
@pytest.mark.xdist_group(name="serial_viewport_tests")
def test_set_viewport_by_device_headless(device: DeviceViewportSize, browser_default: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.viewport.set.size_by_device(device)
    width_check, height_check = browser.viewport.get.size()
    assert device.width == width_check
    assert device.height == height_check
