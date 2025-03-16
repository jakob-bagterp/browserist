from _helper.type import validate_representation
from _mock_data.ip.test_set_5 import VALID_IPV4_ADDRESS

from browserist.model.type.ip import IPv4


def test_ipv4_type_representation() -> None:
    """Test that the IPv4 tiny type represents itself as a string."""

    validate_representation(IPv4, VALID_IPV4_ADDRESS)
