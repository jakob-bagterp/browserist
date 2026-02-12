import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, xpath, expected",
    [
        (internal_url.CHECKBOXES, "//input[@id='checkbox_checked']", True),
        (internal_url.CHECKBOXES, "//input[@id='checkbox_unchecked']", False),
        (internal_url.CHECKBOXES, does_not_exist.XPATH, False),
        (internal_url.RADIO_BUTTONS, "//input[@id='radio_button_checked']", True),
        (internal_url.RADIO_BUTTONS, "//input[@id='radio_button_unchecked']", False),
        (internal_url.RADIO_BUTTONS, does_not_exist.XPATH, False),
    ],
)
def test_check_if_is_selected(url: str, xpath: str, expected: bool, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.check_if.is_selected(xpath) is expected
