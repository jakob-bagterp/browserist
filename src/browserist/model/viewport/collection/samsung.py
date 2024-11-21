from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class SamsungDevices:
    """Viewport sizes for common Samsung devices.

    Example:
        ```python title="" linenums="1" hl_lines="3 6"
        from browserist import Browser, BrowserSettings, common_devices

        galaxy_s8_plus = common_devices.Samsung.GALAXY_S8_PLUS
        settings = BrowserSettings(
            headless=True,
            viewport=galaxy_s8_plus)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    GALAXY_J7 = DeviceViewportSize(360, 640)
    GALAXY_J6 = DeviceViewportSize(360, 640)
    GALAXY_J3 = DeviceViewportSize(360, 640)

    GALAXY_S9_PLUS = DeviceViewportSize(412, 846)
    GALAXY_S9 = DeviceViewportSize(360, 740)

    GALAXY_S8_PLUS = DeviceViewportSize(412, 846)
    GALAXY_S8 = DeviceViewportSize(360, 740)

    GALAXY_S7_EDGE = DeviceViewportSize(360, 640)
    GALAXY_S7 = DeviceViewportSize(360, 640)

    GALAXY_S20_ULTRA = DeviceViewportSize(412, 915)

    GALAXY_FOLD = DeviceViewportSize(280, 653)

    GALAXY_A51_71 = DeviceViewportSize(412, 914)
