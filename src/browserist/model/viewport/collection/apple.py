from dataclasses import dataclass

from ..device import DeviceViewportSize

# Reference: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Displays/Displays.html


@dataclass(slots=True, frozen=True)
class AppleDevices:
    """Viewport sizes for common Apple devices.

    Example:
        ```python title="" linenums="1" hl_lines="3 6"
        from browserist import Browser, BrowserSettings, common_devices

        iphone_x = common_devices.Apple.IPHONE_X
        settings = BrowserSettings(
            headless=True,
            viewport=iphone_x)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    IPHONE_15_PRO_MAX = DeviceViewportSize(430, 932)
    IPHONE_15_PRO = DeviceViewportSize(393, 852)
    IPHONE_15_PLUS = DeviceViewportSize(430, 932)
    IPHONE_15 = DeviceViewportSize(393, 852)

    IPHONE_14_PRO_MAX = DeviceViewportSize(430, 932)
    IPHONE_14_PRO = DeviceViewportSize(393, 852)
    IPHONE_14_PLUS = DeviceViewportSize(428, 926)
    IPHONE_14 = DeviceViewportSize(390, 844)

    IPHONE_13_PRO_MAX = DeviceViewportSize(428, 926)
    IPHONE_13_PRO = DeviceViewportSize(390, 844)
    IPHONE_13_MINI = DeviceViewportSize(375, 812)
    IPHONE_13 = DeviceViewportSize(390, 844)

    IPHONE_12_PRO_MAX = DeviceViewportSize(428, 926)
    IPHONE_12_PRO = DeviceViewportSize(390, 844)
    IPHONE_12_MINI = DeviceViewportSize(375, 812)
    IPHONE_12 = DeviceViewportSize(390, 844)

    IPHONE_11_PRO_MAX = DeviceViewportSize(414, 896)
    IPHONE_11_PRO = DeviceViewportSize(375, 812)
    IPHONE_11 = DeviceViewportSize(414, 896)

    IPHONE_XS_MAX = DeviceViewportSize(414, 896)
    IPHONE_XS = DeviceViewportSize(375, 812)
    IPHONE_XR = DeviceViewportSize(414, 896)
    IPHONE_X = DeviceViewportSize(375, 812)

    IPHONE_8_PLUS = DeviceViewportSize(414, 736)
    IPHONE_8 = DeviceViewportSize(375, 667)

    IPHONE_7_PLUS = DeviceViewportSize(414, 736)
    IPHONE_7 = DeviceViewportSize(375, 667)

    IPHONE_6S_PLUS = DeviceViewportSize(375, 667)
    IPHONE_6S = DeviceViewportSize(375, 667)
    IPHONE_6_PLUS = DeviceViewportSize(375, 667)
    IPHONE_6 = DeviceViewportSize(375, 667)

    IPHONE_SE_3RD_GEN = DeviceViewportSize(375, 667)
    IPHONE_SE_2ND_GEN = DeviceViewportSize(375, 667)
    IPHONE_SE_1ST_GEN = DeviceViewportSize(320, 568)

    IPAD_PRO_12_9_INCH_6TH_GEN = DeviceViewportSize(1024, 1366)
    IPAD_PRO_12_9_INCH_5TH_GEN = DeviceViewportSize(1024, 1366)
    IPAD_PRO_12_9_INCH_4TH_GEN = DeviceViewportSize(1024, 1366)
    IPAD_PRO_12_9_INCH_3RD_GEN = DeviceViewportSize(1024, 1366)
    IPAD_PRO_12_9_INCH_2ND_GEN = DeviceViewportSize(1024, 1366)
    IPAD_PRO_12_9_INCH_1ST_GEN = DeviceViewportSize(1024, 1366)

    IPAD_PRO_11_INCH_4TH_GEN = DeviceViewportSize(834, 1194)
    IPAD_PRO_11_INCH_3RD_GEN = DeviceViewportSize(834, 1194)
    IPAD_PRO_11_INCH_2ND_GEN = DeviceViewportSize(834, 1194)
    IPAD_PRO_11_INCH_1ST_GEN = DeviceViewportSize(834, 1194)

    IPAD_PRO_10_5_INCH = DeviceViewportSize(834, 1112)

    IPAD_PRO_9_7_INCH = DeviceViewportSize(768, 1024)

    IPAD_AIR_5TH_GEN = DeviceViewportSize(820, 1180)
    IPAD_AIR_4TH_GEN = DeviceViewportSize(820, 1180)
    IPAD_AIR_3RD_GEN = DeviceViewportSize(834, 1112)
    IPAD_AIR_2ND_GEN = DeviceViewportSize(768, 1024)
    IPAD_AIR_1ST_GEN = DeviceViewportSize(768, 1024)

    IPAD_MINI_6TH_GEN = DeviceViewportSize(744, 1133)
    IPAD_MINI_5TH_GEN = DeviceViewportSize(768, 1024)
    IPAD_MINI_4TH_GEN = DeviceViewportSize(768, 1024)
    IPAD_MINI_3RD_GEN = DeviceViewportSize(768, 1024)
    IPAD_MINI_2ND_GEN = DeviceViewportSize(768, 1024)
    IPAD_MINI_1ST_GEN = DeviceViewportSize(768, 1024)

    IPAD_10TH_GEN = DeviceViewportSize(810, 1080)
    IPAD_9TH_GEN = DeviceViewportSize(810, 1080)
    IPAD_8TH_GEN = DeviceViewportSize(810, 1080)
    IPAD_7TH_GEN = DeviceViewportSize(810, 1080)
    IPAD_6TH_GEN = DeviceViewportSize(768, 1024)
    IPAD_5TH_GEN = DeviceViewportSize(768, 1024)
    IPAD_4TH_GEN = DeviceViewportSize(768, 1024)
    IPAD_3RD_GEN = DeviceViewportSize(768, 1024)
    IPAD_2ND_GEN = DeviceViewportSize(768, 1024)
    IPAD_1ST_GEN = DeviceViewportSize(768, 1024)
