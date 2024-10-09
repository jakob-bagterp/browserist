import socket
from collections.abc import Generator

import pytest

ORIGINAL_SOCKET_CONNECTION = socket.socket.connect


def no_internet_connection(*args, **kwargs):
    """When mocked to `socket.socket.connect`, this emulates no network connection."""


@pytest.fixture(scope="function")
def disable_network() -> Generator[None, None, None]:
    """Disables the network connection to emulate no internet connection."""

    socket.socket.connect = no_internet_connection
    yield
    socket.socket.connect = ORIGINAL_SOCKET_CONNECTION


@pytest.fixture(scope="function")
def enable_network() -> Generator[None, None, None]:
    """Enables the network connection to emulate internet connection."""

    socket.socket.connect = ORIGINAL_SOCKET_CONNECTION
    yield
    socket.socket.connect = no_internet_connection
