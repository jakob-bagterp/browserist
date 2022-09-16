from dataclasses import dataclass

from .device import DeviceScreenSize


@dataclass
class AppleDevices:
    """Reference: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Displays/Displays.html"""

    IPHONE_X: DeviceScreenSize = DeviceScreenSize(1125, 2436)

    IPHONE_8_PLUS: DeviceScreenSize = DeviceScreenSize(1080, 1920)
    IPHONE_8: DeviceScreenSize = DeviceScreenSize(750, 1334)

    IPHONE_7_PLUS: DeviceScreenSize = DeviceScreenSize(1080, 1920)
    IPHONE_7: DeviceScreenSize = DeviceScreenSize(750, 1334)

    IPHONE_6S_PLUS: DeviceScreenSize = DeviceScreenSize(1080, 1920)
    IPHONE_6S: DeviceScreenSize = DeviceScreenSize(1080, 1920)
    IPHONE_6_PLUS: DeviceScreenSize = DeviceScreenSize(1080, 1920)
    IPHONE_6: DeviceScreenSize = DeviceScreenSize(750, 1334)

    IPHONE_SE: DeviceScreenSize = DeviceScreenSize(640, 1136)

    IPAD_PRO_12_9_INCH_2ND_GEN: DeviceScreenSize = DeviceScreenSize(2048, 2732)
    IPAD_PRO_12_9_INCH: DeviceScreenSize = DeviceScreenSize(2048, 2732)
    IPAD_PRO_10_5_INCH: DeviceScreenSize = DeviceScreenSize(2224, 1668)
    IPAD_PRO_9_7_INCH: DeviceScreenSize = DeviceScreenSize(1536, 2048)

    IPAD_AIR_2: DeviceScreenSize = DeviceScreenSize(1536, 2048)
    IPAD_MINI_4: DeviceScreenSize = DeviceScreenSize(1536, 2048)
