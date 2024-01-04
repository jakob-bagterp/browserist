import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, DeviceViewportSize, common_devices


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
def test_set_viewport_by_device_headless(device: DeviceViewportSize, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.EXAMPLE_COM)
    browser.viewport.set.size_by_device(device)
    width_check, height_check = browser.viewport.get.size()
    assert device.width == width_check and device.height == height_check
