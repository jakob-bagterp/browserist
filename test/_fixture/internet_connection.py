import socket

import pytest

_original_connection = socket.socket.connect


def no_internet_connection(*args, **kwargs):
    pass


@pytest.fixture(scope="function")
def disable_network():
    socket.socket.connect = no_internet_connection
    yield
    socket.socket.connect = _original_connection
