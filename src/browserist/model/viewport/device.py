from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class DeviceViewportSize:
    """Class to define viewport size (width and height) of common devices."""

    width: int
    height: int
