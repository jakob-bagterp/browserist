from _helper.url import internal_url

from browserist import Browser

_common_xpath = "html/body"


def test_iframe_switch_to(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    default_page_text_1 = browser.get.text.from_element(_common_xpath)
    browser.iframe.switch_to("//*[@id='howto_iframe']")
    assert browser.get.text.from_element("/html/body/div[1]/div[1]/div[2]") == "Caption Text"
    iframe_page_text = browser.get.text.from_element(_common_xpath)
    browser.iframe.switch_to_original_page()
    default_page_text_2 = browser.get.text.from_element(_common_xpath)
    assert default_page_text_1 == default_page_text_2
    assert default_page_text_1 != iframe_page_text
