from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass
class AppleDevices:
    """Reference: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Displays/Displays.html"""

    IPHONE_X: DeviceViewportSize = DeviceViewportSize(375, 812)

    IPHONE_8_PLUS: DeviceViewportSize = DeviceViewportSize(414, 736)
    IPHONE_8: DeviceViewportSize = DeviceViewportSize(375, 667)

    IPHONE_7_PLUS: DeviceViewportSize = DeviceViewportSize(414, 736)
    IPHONE_7: DeviceViewportSize = DeviceViewportSize(375, 667)

    IPHONE_6S_PLUS: DeviceViewportSize = DeviceViewportSize(375, 667)
    IPHONE_6S: DeviceViewportSize = DeviceViewportSize(375, 667)
    IPHONE_6_PLUS: DeviceViewportSize = DeviceViewportSize(375, 667)
    IPHONE_6: DeviceViewportSize = DeviceViewportSize(375, 667)

    IPHONE_SE: DeviceViewportSize = DeviceViewportSize(320, 568)

    IPAD_PRO_12_9_INCH_2ND_GEN: DeviceViewportSize = DeviceViewportSize(1024, 1366)
    IPAD_PRO_12_9_INCH: DeviceViewportSize = DeviceViewportSize(1024, 1366)
    IPAD_PRO_10_5_INCH: DeviceViewportSize = DeviceViewportSize(1112, 834)
    IPAD_PRO_9_7_INCH: DeviceViewportSize = DeviceViewportSize(768, 1024)

    IPAD_AIR_2: DeviceViewportSize = DeviceViewportSize(768, 1024)
    IPAD_MINI_4: DeviceViewportSize = DeviceViewportSize(768, 1024)
