import pytest
from _mock_data.ip.test_set_5 import VALID_IPV4_ADDRESS

from browserist import helper


@pytest.mark.parametrize(
    "ip_address, expected",
    [
        (VALID_IPV4_ADDRESS, True),
        ("1.2.3.4", True),
        ("invalid_ip_address", False),
        ("256.255.255.255", False),
        ("0.0.0.256", False),
        ("256.255.255.256", False),
        ("256.255.255.255.", False),
        ("0", False),
        ("0.0", False),
        ("0.0.0", False),
        ("0.0.0.0", True),
        ("0.0.0.0.0", False),
        ("255", False),
        ("255.255", False),
        ("255.255.255", False),
        ("255.255.255.255", True),
        ("255.255.255.255.255", False),
    ],
)
def test_helper_ipv4_is_valid(ip_address: str, expected: bool) -> None:
    assert helper.ip.ipv4_is_valid(ip_address) is expected
