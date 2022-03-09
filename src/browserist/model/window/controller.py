from ...browser.window.handle.current import get_current_window_handle
from .handle import WindowHandle


class WindowHandleController:
    def __init__(self, driver: object) -> None:
        self._counter: int = 1
        self._window_handles: list[WindowHandle] = [
            WindowHandle(
                name=str(self._counter),
                id=get_current_window_handle(driver),
            )]
