from dataclasses import dataclass


@dataclass(slots=True)
class DeviceScreenSize:
    width: int
    height: int
