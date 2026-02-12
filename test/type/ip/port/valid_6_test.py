from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.ip.test_set_5 import VALID_IP_PORT

from browserist.exception.ip import IPPortSyntaxError
from browserist.model.type.ip import IPPort


@pytest.mark.parametrize(
    "port, expectation, is_valid_expectation",
    [
        (VALID_IP_PORT, does_not_raise(), True),
        (80, does_not_raise(), True),
        (443, does_not_raise(), True),
        (8080, does_not_raise(), True),
        ("invalid_port", pytest.raises(ValueError), False),
        (0, pytest.raises(IPPortSyntaxError), False),
        (65536, pytest.raises(IPPortSyntaxError), False),
        (-1, pytest.raises(IPPortSyntaxError), False),
        (-65536, pytest.raises(IPPortSyntaxError), False),
    ],
)
def test_ip_port_type_is_valid(port: int, expectation: Any, is_valid_expectation: bool) -> None:
    with expectation:
        port = IPPort(port)
        assert port.is_valid() == is_valid_expectation
