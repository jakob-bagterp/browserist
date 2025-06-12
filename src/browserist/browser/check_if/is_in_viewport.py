from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..tool.execute_script import tool_execute_script


def check_if_is_in_viewport(browser_driver: BrowserDriver, xpath: str) -> bool:
    def get_script(xpath: XPath) -> str:
        return f"""
            var element = document.evaluate('{xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

            if (!element) return false;
            if (1 !== element.nodeType) return false;

            var html = document.documentElement;
            var rect = element.getBoundingClientRect();

            return !!rect &&
                rect.bottom >= 0 &&
                rect.right >= 0 &&
                rect.left <= html.clientWidth &&
                rect.top <= html.clientHeight;
        """

    xpath = XPath(xpath)
    try:
        script = get_script(xpath)
        return bool(tool_execute_script(browser_driver, script))
    except Exception:
        return False
