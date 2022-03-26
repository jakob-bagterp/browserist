from _helper.xpath import VALID_XPATH

from browserist.model.type.xpath import XPath


def test_xpath_type_representation() -> None:
    """Test that the XPath tiny type represents itself as a an XPath string."""

    xpath_input = expected_xpath_output = VALID_XPATH
    xpath_type = XPath(xpath_input)
    assert expected_xpath_output == xpath_type
    assert expected_xpath_output == xpath_type.value
