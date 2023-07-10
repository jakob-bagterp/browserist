import re

from ..model.window.handle import WindowHandle


def name_already_exists(name: str, window_handles: list[WindowHandle]) -> bool:
    return name in [window_handle.name for window_handle in window_handles]


def id_already_exists(id: str, window_handles: list[WindowHandle]) -> bool:
    return id in [window_handle.id for window_handle in window_handles]


WINDOW_HANDLE_ID_PATTERN = re.compile(r"^(CDwindow-)?[A-Z0-9]{32}$")


def is_valid_id(id: str) -> bool:
    """Checks if handle ID is similar to this pattern: CDwindow-8088CB616D7499360039D98453AE91FC"""

    return bool(WINDOW_HANDLE_ID_PATTERN.match(id))
