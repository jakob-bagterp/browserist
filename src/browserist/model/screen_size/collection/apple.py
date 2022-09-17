from dataclasses import dataclass

from ..device import DeviceScreenSize


@dataclass
class AppleDevices:
    """Reference: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Displays/Displays.html"""

    IPHONE_X: DeviceScreenSize = DeviceScreenSize(375, 812)

    IPHONE_8_PLUS: DeviceScreenSize = DeviceScreenSize(414, 736)
    IPHONE_8: DeviceScreenSize = DeviceScreenSize(375, 667)

    IPHONE_7_PLUS: DeviceScreenSize = DeviceScreenSize(414, 736)
    IPHONE_7: DeviceScreenSize = DeviceScreenSize(375, 667)

    IPHONE_6S_PLUS: DeviceScreenSize = DeviceScreenSize(375, 667)
    IPHONE_6S: DeviceScreenSize = DeviceScreenSize(375, 667)
    IPHONE_6_PLUS: DeviceScreenSize = DeviceScreenSize(375, 667)
    IPHONE_6: DeviceScreenSize = DeviceScreenSize(375, 667)

    IPHONE_SE: DeviceScreenSize = DeviceScreenSize(320, 568)

    IPAD_PRO_12_9_INCH_2ND_GEN: DeviceScreenSize = DeviceScreenSize(1024, 1366)
    IPAD_PRO_12_9_INCH: DeviceScreenSize = DeviceScreenSize(1024, 1366)
    IPAD_PRO_10_5_INCH: DeviceScreenSize = DeviceScreenSize(1112, 834)
    IPAD_PRO_9_7_INCH: DeviceScreenSize = DeviceScreenSize(768, 1024)

    IPAD_AIR_2: DeviceScreenSize = DeviceScreenSize(768, 1024)
    IPAD_MINI_4: DeviceScreenSize = DeviceScreenSize(768, 1024)
