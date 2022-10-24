from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass
class GoogleDevices:
    PIXEL_5: DeviceViewportSize = DeviceViewportSize(393, 851)
    NEST_HUB: DeviceViewportSize = DeviceViewportSize(1024, 600)
    NEST_HUB_MAX: DeviceViewportSize = DeviceViewportSize(1280, 800)
