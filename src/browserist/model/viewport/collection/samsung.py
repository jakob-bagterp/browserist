from dataclasses import dataclass

from ..device import DeviceViewport


@dataclass
class SamsungDevices:
    GALAXY_S8_PLUS: DeviceViewport = DeviceViewport(360, 740)
    GALAXY_S20_ULTRA: DeviceViewport = DeviceViewport(412, 915)
    GALAXY_FOLD: DeviceViewport = DeviceViewport(280, 653)
    GALAXY_A51_71: DeviceViewport = DeviceViewport(412, 914)
