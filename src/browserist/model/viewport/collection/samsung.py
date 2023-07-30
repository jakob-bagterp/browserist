from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class SamsungDevices:
    """Viewport sizes for common Samsung devices.

    Example:
        ```python title=""
        from browserist import Browser, BrowserSettings, common_devices

        settings = BrowserSettings(headless = True)
        galaxy_s8_plus = common_devices.Samsung.GALAXY_S8_PLUS

        with Browser(settings) as browser:
            browser.viewport.set.size_by_device(galaxy_s8_plus)
            browser.open.url("https://example.com")
        ```
    """

    GALAXY_S8_PLUS = DeviceViewportSize(360, 740)
    GALAXY_S20_ULTRA = DeviceViewportSize(412, 915)
    GALAXY_FOLD = DeviceViewportSize(280, 653)
    GALAXY_A51_71 = DeviceViewportSize(412, 914)
