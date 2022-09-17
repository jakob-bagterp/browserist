from dataclasses import dataclass


@dataclass(slots=True)
class DeviceViewport:
    """Class to define viewport size (width and height) of common devices."""

    width: int
    height: int
