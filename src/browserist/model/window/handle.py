from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WindowHandle:
    """Data class used when opening a new tab/window, so the user can define a humanised name while the actual ID of the tab/window is handled by the system in the background."""

    name: str
    id: str
