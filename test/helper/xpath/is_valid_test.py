import pytest

from browserist import helper


@pytest.mark.parametrize("xpath, expected", [
    ("//*[@id='react-root']/section", True),
    ("//*[[@id='react-root']/section", False),
    ("//*[@id='react-root']\\section", False),
])
def test_helper_window_handle_is_valid_id(xpath: str, expected: bool) -> None:
    assert helper.xpath.is_valid(xpath) is expected
