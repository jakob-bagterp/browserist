from _helper.type import validate_bypass
from _mock_data.xpath.test_set_3 import VALID_XPATH

from browserist.model.type.xpath import XPath


def test_xpath_type_bypass_if_already_xpath() -> None:
    """Test that if an input already is a validated XPath element, bypass and don't create a new object."""

    validate_bypass(XPath, VALID_XPATH)
