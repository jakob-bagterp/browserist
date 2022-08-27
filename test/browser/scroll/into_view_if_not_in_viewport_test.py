from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout

W3SCHOOLS_COM_FOOTER_XPATH = "//*[@id='main']/footer"


def test_scroll_into_view_if_not_in_viewport(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.W3SCHOOLS_COM)
    assert browser.check_if.is_in_viewport(W3SCHOOLS_COM_FOOTER_XPATH) is False
    browser.scroll.into_view_if_not_in_viewport(W3SCHOOLS_COM_FOOTER_XPATH, timeout.VERY_SHORT, delay_seconds=0)
    assert browser.check_if.is_in_viewport(W3SCHOOLS_COM_FOOTER_XPATH) is True
