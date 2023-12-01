import socket

import pytest

ORIGINAL_SOCKET_CONNECTION = socket.socket.connect


def no_internet_connection(*args, **kwargs):
    """When mocked to `socket.socket.connect`, this emulates no network connection."""


@pytest.fixture(scope="function")
def disable_network():
    socket.socket.connect = no_internet_connection
    yield
    socket.socket.connect = ORIGINAL_SOCKET_CONNECTION
