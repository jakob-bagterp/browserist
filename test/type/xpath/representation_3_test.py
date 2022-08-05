from _helper.type import validate_representation
from _mock_data.xpath.test_set_3 import VALID_XPATH

from browserist.model.type.xpath import XPath


def test_xpath_type_representation() -> None:
    """Test that the XPath tiny type represents itself as a string."""

    validate_representation(XPath, VALID_XPATH)
