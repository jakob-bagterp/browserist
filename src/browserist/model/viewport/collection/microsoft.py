from dataclasses import dataclass

from ..device import DeviceViewport


@dataclass
class MicrosoftDevices:
    SURFACE_PRO_7: DeviceViewport = DeviceViewport(912, 1368)
    SURFACE_DUO: DeviceViewport = DeviceViewport(540, 720)
