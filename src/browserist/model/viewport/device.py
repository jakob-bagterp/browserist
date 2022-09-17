from dataclasses import dataclass


@dataclass(slots=True)
class DeviceViewport:
    width: int
    height: int
