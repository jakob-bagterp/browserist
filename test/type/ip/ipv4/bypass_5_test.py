from _helper.type import validate_bypass
from _mock_data.ip.test_set_5 import VALID_IPV4_ADDRESS

from browserist.model.type.ip import IPv4


def test_ipv4_type_bypass_if_already_ipv4_address() -> None:
    """Test that if an input already is a validated IPv4 element, bypass and don't create a new object."""

    validate_bypass(IPv4, VALID_IPV4_ADDRESS)
