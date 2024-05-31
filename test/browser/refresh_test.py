from _helper import script
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH

from browserist import Browser

REMOVE_HEADLINE_JAVASCRIPT = script.remove_element(MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH)


def test_refresh(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    assert browser.check_if.does_exist(MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH) is True
    browser.tool.execute_script(REMOVE_HEADLINE_JAVASCRIPT)
    assert browser.check_if.does_exist(MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH) is False
    browser.refresh()
    assert browser.check_if.does_exist(MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH) is True
