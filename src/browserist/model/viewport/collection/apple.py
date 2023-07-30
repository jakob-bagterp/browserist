from dataclasses import dataclass

from ..device import DeviceViewportSize

# Reference: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Displays/Displays.html


@dataclass(slots=True, frozen=True)
class AppleDevices:
    """Viewport sizes for common Apple devices.

    Example:
        ```python title=""
        from browserist import Browser, BrowserSettings, common_devices

        settings = BrowserSettings(headless = True)
        iphone_x = common_devices.Apple.IPHONE_X

        with Browser(settings) as browser:
            browser.viewport.set.size_by_device(iphone_x)
            browser.open.url("https://example.com")
        ```
    """

    IPHONE_X = DeviceViewportSize(375, 812)

    IPHONE_8_PLUS = DeviceViewportSize(414, 736)
    IPHONE_8 = DeviceViewportSize(375, 667)

    IPHONE_7_PLUS = DeviceViewportSize(414, 736)
    IPHONE_7 = DeviceViewportSize(375, 667)

    IPHONE_6S_PLUS = DeviceViewportSize(375, 667)
    IPHONE_6S = DeviceViewportSize(375, 667)
    IPHONE_6_PLUS = DeviceViewportSize(375, 667)
    IPHONE_6 = DeviceViewportSize(375, 667)

    IPHONE_SE = DeviceViewportSize(320, 568)

    IPAD_PRO_12_9_INCH_2ND_GEN = DeviceViewportSize(1024, 1366)
    IPAD_PRO_12_9_INCH = DeviceViewportSize(1024, 1366)
    IPAD_PRO_10_5_INCH = DeviceViewportSize(1112, 834)
    IPAD_PRO_9_7_INCH = DeviceViewportSize(768, 1024)

    IPAD_AIR_2 = DeviceViewportSize(768, 1024)
    IPAD_MINI_4 = DeviceViewportSize(768, 1024)
