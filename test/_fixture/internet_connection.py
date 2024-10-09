import socket
from collections.abc import Generator
from types import TracebackType

import pytest

ORIGINAL_SOCKET_CONNECTION = socket.socket.connect


def no_internet_connection(*args, **kwargs):
    """When mocked to `socket.socket.connect`, this emulates no network connection."""


class NetworkDisabler:
    """Context manager to disable the network connection to emulate no internet connection."""

    def __enter__(self):
        socket.socket.connect = no_internet_connection

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        socket.socket.connect = ORIGINAL_SOCKET_CONNECTION


@pytest.fixture(scope="function")
def disable_network() -> Generator[None, None, None]:
    """Disables the network connection to emulate no internet connection."""

    with NetworkDisabler():
        yield


@pytest.fixture(scope="function")
def enable_network() -> Generator[None, None, None]:
    """Enables the network connection to emulate internet connection."""

    socket.socket.connect = ORIGINAL_SOCKET_CONNECTION
    yield
