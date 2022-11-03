from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass
class MicrosoftDevices:
    SURFACE_PRO_7 = DeviceViewportSize(912, 1368)
    SURFACE_DUO = DeviceViewportSize(540, 720)
