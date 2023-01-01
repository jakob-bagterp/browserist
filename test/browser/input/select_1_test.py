from _config.browser_settings import default
from _mock_data.url import internal_url
from _mock_data.xpath import xpath

from browserist import Browser


def test_select_input_field() -> None:
    with Browser(default.DEFAULT) as browser:
        browser.open.url(internal_url.DROPDOWN_SELECTOR)
        assert browser.get.attribute.value(xpath.DropDownSeletor.DROPDOWN_OPTIONS, "value") == "option1"
        browser.input.select(xpath.DropDownSeletor.OPTION_2)
        assert browser.get.attribute.value(xpath.DropDownSeletor.DROPDOWN_OPTIONS, "value") == "option2"
        browser.input.select(xpath.DropDownSeletor.OPTION_3)
        assert browser.get.attribute.value(xpath.DropDownSeletor.DROPDOWN_OPTIONS, "value") == "option3"
        browser.input.select(xpath.DropDownSeletor.OPTION_4)
        assert browser.get.attribute.value(xpath.DropDownSeletor.DROPDOWN_OPTIONS, "value") == "option4"
