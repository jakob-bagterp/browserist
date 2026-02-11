import _helper
import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, DeviceViewportSize, common_devices
from browserist.helper import operating_system


@pytest.mark.parametrize("device", [
    common_devices.Apple.IPHONE_6,
    common_devices.Apple.IPHONE_SE_1ST_GEN,
    common_devices.Apple.IPAD_AIR_2ND_GEN,
    common_devices.Apple.IPAD_PRO_9_7_INCH,
    common_devices.Google.NEST_HUB_MAX,
    common_devices.Huawei.P40_LITE,
    common_devices.Microsoft.SURFACE_PRO_7,
    common_devices.OnePlus.ONEPLUS_8_PRO,
    common_devices.Oppo.F1_PLUS,
    common_devices.Samsung.GALAXY_S8_PLUS,
    common_devices.Vivo.Y20,
    common_devices.Xiaomi.MI_10_PRO,
])
@pytest.mark.xdist_group(name="serial_viewport_tests")
def test_set_viewport_by_device_headless(device: DeviceViewportSize, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    browser.viewport.set.size_by_device(device)
    width_check, height_check = browser.viewport.get.size()
    if operating_system.is_macos() or operating_system.is_windows():
        minimum_width = _helper.tolerance.deduct(device.width, 50)
        maximum_width = _helper.tolerance.add(device.width, 70)
        assert minimum_width < width_check < maximum_width
        minimum_height = _helper.tolerance.deduct(device.height, 50)
        maximum_height = _helper.tolerance.add(device.height, 50)
        assert minimum_height < height_check < maximum_height
    else:
        assert device.width == width_check
        assert device.height == height_check
