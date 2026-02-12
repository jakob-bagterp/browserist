import pytest
from _mock_data.ip.test_set_5 import VALID_IP_PORT

from browserist import helper


@pytest.mark.parametrize(
    "port, expected",
    [
        (VALID_IP_PORT, True),
        (0, False),
        (1, True),
        (65535, True),
        (65536, False),
        (-1, False),
        (-65535, False),
        (-65536, False),
        (80, True),
        (443, True),
        (8080, True),
    ],
)
def test_helper_port_is_valid(port: int, expected: bool) -> None:
    assert helper.ip.port_is_valid(port) is expected
