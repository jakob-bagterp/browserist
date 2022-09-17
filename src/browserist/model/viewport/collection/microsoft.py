from dataclasses import dataclass

from ..device import DeviceScreenSize


@dataclass
class MicrosoftDevices:
    SURFACE_PRO_7: DeviceScreenSize = DeviceScreenSize(912, 1368)
    SURFACE_DUO: DeviceScreenSize = DeviceScreenSize(540, 720)
