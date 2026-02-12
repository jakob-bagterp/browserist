import pytest
from _mock_data.xpath.constant import INVALID_XPATH, VALID_XPATH

from browserist import helper


@pytest.mark.parametrize(
    "xpath, expected",
    [
        (VALID_XPATH, True),
        (INVALID_XPATH, False),
        ("//*[@id='react-root']/section", True),
        ("//*[[@id='react-root']/section", False),
        ("//*[@id='react-root']\\section", False),
    ],
)
def test_helper_is_valid_xpath(xpath: str, expected: bool) -> None:
    assert helper.xpath.is_valid(xpath) is expected
