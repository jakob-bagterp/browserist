from dataclasses import dataclass

from ..device import DeviceScreenSize


@dataclass
class GoogleDevices:
    PIXEL_5: DeviceScreenSize = DeviceScreenSize(393, 851)
    NEST_HUB: DeviceScreenSize = DeviceScreenSize(1024, 600)
    NEST_HUB_MAX: DeviceScreenSize = DeviceScreenSize(1280, 800)
