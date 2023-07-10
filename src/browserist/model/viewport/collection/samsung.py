from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class SamsungDevices:
    GALAXY_S8_PLUS = DeviceViewportSize(360, 740)
    GALAXY_S20_ULTRA = DeviceViewportSize(412, 915)
    GALAXY_FOLD = DeviceViewportSize(280, 653)
    GALAXY_A51_71 = DeviceViewportSize(412, 914)
