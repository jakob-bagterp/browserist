from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class MicrosoftDevices:
    SURFACE_PRO_7 = DeviceViewportSize(912, 1368)
    SURFACE_DUO = DeviceViewportSize(540, 720)
