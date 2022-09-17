from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass
class SamsungDevices:
    GALAXY_S8_PLUS: DeviceViewportSize = DeviceViewportSize(360, 740)
    GALAXY_S20_ULTRA: DeviceViewportSize = DeviceViewportSize(412, 915)
    GALAXY_FOLD: DeviceViewportSize = DeviceViewportSize(280, 653)
    GALAXY_A51_71: DeviceViewportSize = DeviceViewportSize(412, 914)
