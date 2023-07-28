from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class MicrosoftDevices:
    """Viewport sizes for common Microsoft devices."""

    SURFACE_PRO_7 = DeviceViewportSize(912, 1368)
    SURFACE_DUO = DeviceViewportSize(540, 720)
