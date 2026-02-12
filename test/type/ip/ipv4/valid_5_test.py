from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.ip.test_set_5 import VALID_IPV4_ADDRESS

from browserist.exception.ip import IPv4SyntaxError
from browserist.model.type.ip import IPv4


@pytest.mark.parametrize(
    "ip_address, expectation, is_valid_expectation",
    [
        (VALID_IPV4_ADDRESS, does_not_raise(), True),
        ("invalid_ip_address", pytest.raises(IPv4SyntaxError), False),
        (1234, pytest.raises(TypeError), False),
        ("256.255.255.255", pytest.raises(IPv4SyntaxError), False),
    ],
)
def test_ipv4_type_is_valid(ip_address: str, expectation: Any, is_valid_expectation: bool) -> None:
    with expectation:
        ip_address = IPv4(ip_address)
        assert ip_address.is_valid() == is_valid_expectation
