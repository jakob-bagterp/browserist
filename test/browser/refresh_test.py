from _helper import script
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser

HEADLINE_XPATH = "/html/body/div/h1"

REMOVE_HEADLINE_JAVASCRIPT = script.remove_element(HEADLINE_XPATH)


def test_refresh(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.check_if.does_exist(HEADLINE_XPATH) is True
    browser.tool.execute_script(REMOVE_HEADLINE_JAVASCRIPT)
    assert browser.check_if.does_exist(HEADLINE_XPATH) is False
    browser.refresh()
    assert browser.check_if.does_exist(HEADLINE_XPATH) is True
