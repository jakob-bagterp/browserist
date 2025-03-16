from _helper.type import validate_bypass
from _mock_data.ip.test_set_5 import VALID_IP_PORT

from browserist.model.type.ip import IPPort


def test_ip_port_type_bypass_if_already_ip_port() -> None:
    """Test that if an input already is a validated IPPort element, bypass and don't create a new object."""

    validate_bypass(IPPort, VALID_IP_PORT)
