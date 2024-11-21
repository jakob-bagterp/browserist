from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class OnePlusDevices:
    """Viewport sizes for common OnePlus devices.

    Example:
        ```python title="" linenums="1" hl_lines="3 6"
        from browserist import Browser, BrowserSettings, common_devices

        oneplus_8_pro = common_devices.OnePlus.ONEPLUS_8_PRO
        settings = BrowserSettings(
            headless=True,
            viewport=oneplus_8_pro)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    ONEPLUS_9_PRO = DeviceViewportSize(412, 919)
    ONEPLUS_9 = DeviceViewportSize(412, 915)

    ONEPLUS_8_PRO = DeviceViewportSize(412, 906)
    ONEPLUS_8 = DeviceViewportSize(412, 915)

    ONEPLUS_7T_PRO = DeviceViewportSize(412, 892)
    ONEPLUS_7T = DeviceViewportSize(412, 914)
    ONEPLUS_7_PRO = DeviceViewportSize(412, 892)
    ONEPLUS_7 = DeviceViewportSize(412, 892)

    ONEPLUS_6 = DeviceViewportSize(412, 869)
    ONEPLUS_6T = DeviceViewportSize(412, 892)

    NORD = DeviceViewportSize(412, 915)
