from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout


def test_tool_execute_script(browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.NO_BODY)
    elements = browser.get.elements_by_tag("body", timeout.BYPASS)
    # The browser will always add a body element to the page, even though it is not present in the HTML page:
    assert len(elements) == 1
    script_remove_body_element = """
        var html = document.getElementsByTagName('html');
        var body = html[0];
        body.removeChild(document.body);
    """
    browser.tool.execute_script(script_remove_body_element)
    elements = browser.get.elements_by_tag("body", timeout.BYPASS)
    assert len(elements) == 0
