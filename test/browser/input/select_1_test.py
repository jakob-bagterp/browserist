from _config.browser_settings import default
from _mock_data.url import internal_url
from _mock_data.xpath.drop_down_seletor import DROPDOWN_OPTIONS_XPATH, OPTION_2_XPATH, OPTION_3_XPATH, OPTION_4_XPATH

from browserist import Browser


def test_select_input_field() -> None:
    with Browser(default.DEFAULT) as browser:
        browser.open.url(internal_url.DROPDOWN_SELECTOR)
        assert browser.get.attribute.value(DROPDOWN_OPTIONS_XPATH, "value") == "option1"
        browser.input.select(OPTION_2_XPATH)
        assert browser.get.attribute.value(DROPDOWN_OPTIONS_XPATH, "value") == "option2"
        browser.input.select(OPTION_3_XPATH)
        assert browser.get.attribute.value(DROPDOWN_OPTIONS_XPATH, "value") == "option3"
        browser.input.select(OPTION_4_XPATH)
        assert browser.get.attribute.value(DROPDOWN_OPTIONS_XPATH, "value") == "option4"
