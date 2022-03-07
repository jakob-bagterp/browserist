from ..model.window.handle import WindowHandle


def name_already_exists(name: str, window_handles: list[WindowHandle]) -> bool:
    return name in [window_handle.name for window_handle in window_handles]


def id_already_exists(id: str, window_handles: list[WindowHandle]) -> bool:
    return id in [window_handle.id for window_handle in window_handles]
