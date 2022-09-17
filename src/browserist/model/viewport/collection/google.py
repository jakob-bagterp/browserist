from dataclasses import dataclass

from ..device import DeviceViewport


@dataclass
class GoogleDevices:
    PIXEL_5: DeviceViewport = DeviceViewport(393, 851)
    NEST_HUB: DeviceViewport = DeviceViewport(1024, 600)
    NEST_HUB_MAX: DeviceViewport = DeviceViewport(1280, 800)
