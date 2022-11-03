from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class GoogleDevices:
    PIXEL_5 = DeviceViewportSize(393, 851)
    NEST_HUB = DeviceViewportSize(1024, 600)
    NEST_HUB_MAX = DeviceViewportSize(1280, 800)
