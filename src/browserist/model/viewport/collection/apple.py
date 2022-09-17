from dataclasses import dataclass

from ..device import DeviceViewport


@dataclass
class AppleDevices:
    """Reference: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Displays/Displays.html"""

    IPHONE_X: DeviceViewport = DeviceViewport(375, 812)

    IPHONE_8_PLUS: DeviceViewport = DeviceViewport(414, 736)
    IPHONE_8: DeviceViewport = DeviceViewport(375, 667)

    IPHONE_7_PLUS: DeviceViewport = DeviceViewport(414, 736)
    IPHONE_7: DeviceViewport = DeviceViewport(375, 667)

    IPHONE_6S_PLUS: DeviceViewport = DeviceViewport(375, 667)
    IPHONE_6S: DeviceViewport = DeviceViewport(375, 667)
    IPHONE_6_PLUS: DeviceViewport = DeviceViewport(375, 667)
    IPHONE_6: DeviceViewport = DeviceViewport(375, 667)

    IPHONE_SE: DeviceViewport = DeviceViewport(320, 568)

    IPAD_PRO_12_9_INCH_2ND_GEN: DeviceViewport = DeviceViewport(1024, 1366)
    IPAD_PRO_12_9_INCH: DeviceViewport = DeviceViewport(1024, 1366)
    IPAD_PRO_10_5_INCH: DeviceViewport = DeviceViewport(1112, 834)
    IPAD_PRO_9_7_INCH: DeviceViewport = DeviceViewport(768, 1024)

    IPAD_AIR_2: DeviceViewport = DeviceViewport(768, 1024)
    IPAD_MINI_4: DeviceViewport = DeviceViewport(768, 1024)
