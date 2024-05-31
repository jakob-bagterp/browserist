import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.drop_down_seletor import OPTION_1_XPATH, OPTION_2_XPATH, OPTION_3_XPATH, OPTION_4_XPATH

from browserist import Browser


@pytest.mark.parametrize("xpath, expected_value", [
    (OPTION_1_XPATH, "option1"),
    (OPTION_2_XPATH, "option2"),
    (OPTION_3_XPATH, "option3"),
    (OPTION_4_XPATH, "option4"),
])
def test_select_input_field(xpath: str, expected_value: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.DROPDOWN_SELECTOR)
    assert browser.get.attribute.value(xpath, "value") == expected_value
