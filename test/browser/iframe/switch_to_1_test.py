from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser

XPATH_BODY = "html/body"


def test_iframe_switch_to(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    default_page_text_1 = browser.get.text(XPATH_BODY)
    browser.iframe.switch_to("//*[@id='howto_iframe']")
    assert browser.get.text("/html/body/div[1]/div[1]/div[2]") == "Caption Text"
    iframe_page_text = browser.get.text(XPATH_BODY)
    browser.iframe.switch_to_original_page()
    default_page_text_2 = browser.get.text(XPATH_BODY)
    assert default_page_text_1 == default_page_text_2
    assert default_page_text_1 != iframe_page_text
