from dataclasses import dataclass

from ..device import DeviceScreenSize


@dataclass
class SamsungDevices:
    GALAXY_S8_PLUS: DeviceScreenSize = DeviceScreenSize(360, 740)
    GALAXY_S20_ULTRA: DeviceScreenSize = DeviceScreenSize(412, 915)
    GALAXY_FOLD: DeviceScreenSize = DeviceScreenSize(280, 653)
    GALAXY_A51_71: DeviceScreenSize = DeviceScreenSize(412, 914)
