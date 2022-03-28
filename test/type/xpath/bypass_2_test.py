from _helper.xpath.test_set_2 import VALID_XPATH

from browserist.model.type.xpath import XPath


def test_xpath_type_bypass_if_already_xpath() -> None:
    """Test that if an input already is a validated XPath element, bypass and don't create a new object."""

    xpath_type = XPath(VALID_XPATH)
    assert xpath_type is XPath(xpath_type)
    assert XPath(VALID_XPATH) is not XPath(VALID_XPATH)
