from _helper import internal_url

from browserist import Browser

def test_tool_count_elements(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    assert browser.tool.count_elements("/html/body/div/p") == 2
