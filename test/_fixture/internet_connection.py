import socket
from collections.abc import Generator
from types import TracebackType

import pytest


class NetworkDisabler:
    """Context manager to disable the network connection to emulate no internet connection."""

    def __init__(self) -> None:
        self._original_socket_connection = socket.socket.connect

    def __enter__(self):
        socket.socket.connect = self._no_internet_connection

    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None:
        socket.socket.connect = self._original_socket_connection

    def _no_internet_connection(*args, **kwargs) -> None:
        """When mocked to `socket.socket.connect`, this emulates no network connection."""


@pytest.fixture(scope="function")
def disable_network() -> Generator[None, None, None]:
    """Disables the network connection to emulate no internet connection."""

    with NetworkDisabler():
        yield
