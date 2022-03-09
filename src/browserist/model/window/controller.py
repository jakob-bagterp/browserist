from ... import helper
from ...browser.window.handle.current import get_current_window_handle
from ...exception.window_handle import (WindowHandleIdNotFoundError, WindowHandleIdNotUniqueError,
                                        WindowHandleIdNotValidError, WindowHandleNameNotFoundError,
                                        WindowHandleNameNotUniqueError)
from .handle import WindowHandle


class WindowHandleController:
    def __init__(self, driver: object) -> None:
        self._counter: int = 1
        self._window_handles: list[WindowHandle] = [
            WindowHandle(
                name=str(self._counter),
                id=get_current_window_handle(driver),
            )]

    def add_handle(self, id: str, name: str | None = None) -> None:
        """Add new window handle to list."""

        if not helper.window_handle.is_valid_id(id):
            raise WindowHandleIdNotValidError(id)
        if helper.window_handle.id_already_exists(id, self._window_handles):
            raise WindowHandleIdNotUniqueError(id)
        self._counter += 1
        if name is None:
            name = str(self._counter)
        if helper.window_handle.name_already_exists(name, self._window_handles):
            raise WindowHandleNameNotUniqueError(name)
        self._window_handles.append(WindowHandle(name, id))

    def remove_handle_by_id(self, id: str) -> None:
        """Remove window handle ID."""

        checksum = self.count()
        if not helper.window_handle.is_valid_id(id):
            raise WindowHandleIdNotValidError(id)
        for window_handle in self._window_handles:
            if id == window_handle.id:
                self._window_handles.remove(window_handle)
        if self.count() != checksum - 1:
            raise WindowHandleIdNotFoundError(id)

    def remove_handle_by_name(self, name: str) -> None:
        """Remove window handle name."""

        checksum = self.count()
        for window_handle in self._window_handles:
            if name == window_handle.name:
                self._window_handles.remove(window_handle)
        if self.count() != checksum - 1:
            raise WindowHandleNameNotFoundError(name)
        # TODO: Should original window have special case so it can't be removed? Or should removed original window be handled as special case elsewhere?

    def get_handle_id_by_name(self, name: str) -> str:
        """Get window handle ID by name."""

        for window_handle in self._window_handles:
            if name == window_handle.name:
                return window_handle.id
        raise WindowHandleNameNotFoundError(name)

    def get_handle_name_by_id(self, id: str) -> str:
        """Get window handle name by ID."""

        for window_handle in self._window_handles:
            if id == window_handle.id:
                return window_handle.name
        raise WindowHandleIdNotFoundError(id)

    def count(self) -> int:
        """Get current total number of window handles."""

        return len(self._window_handles)
