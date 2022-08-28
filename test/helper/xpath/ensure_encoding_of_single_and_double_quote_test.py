import pytest
from _mock_data.xpath.test_set_3 import VALID_XPATH

from browserist import helper


@pytest.mark.parametrize("xpath, expected_output", [
    (VALID_XPATH, VALID_XPATH),
    ("//button[contains(text(), \"Double Quotes\")]", "//button[contains(text(), 'Double Quotes')]"),
    ('//button[contains(text(), "Double Quotes")]', "//button[contains(text(), 'Double Quotes')]"),
    ("//div[@name=\"Bob's Pizza\"]", "//div[@name=concat('\"Bob', '\'s Pizza', '\"')]"),
    ("//div[@name='\"Pizza\" Pam']", "//div[@name=concat('\'', '\"Pizza\" Pam', '\'')]"),
    ('//div[@name="Shouldn\'t Be"]', "//div[@name=concat('\"Shouldn', '\'t Be', '\"')]"),
])
def test_ensure_encoding_of_single_and_double_quotes(xpath: str, expected_output: str) -> None:
    assert helper.xpath.is_valid(xpath)
    assert helper.xpath.is_valid(expected_output)
    assert helper.xpath.ensure_encoding_of_single_and_double_quotes(xpath) == expected_output
