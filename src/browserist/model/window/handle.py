from dataclasses import dataclass


@dataclass(frozen=True)
class WindowHandle:
    """Object that let's the user define a humanised name for a tab/window while the actual ID is handled by the system in the background."""

    name: str
    id: str
