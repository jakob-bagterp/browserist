from _helper.type import validate_representation_int
from _mock_data.ip.test_set_5 import VALID_IP_PORT

from browserist.model.type.ip import IPPort


def test_ip_port_type_representation() -> None:
    """Test that the IPPort tiny type represents itself as a string."""

    validate_representation_int(IPPort, VALID_IP_PORT)
