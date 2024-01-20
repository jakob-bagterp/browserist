from ... import helper
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..input.value import input_value


def prompt_and_input_value(browser_driver: BrowserDriver, xpath: str, prompt_message: str, validate_input_regex: str | None, timeout: float) -> None:
    xpath = XPath(xpath)
    value = helper.terminal.prompt_user_for_value(prompt_message, validate_input_regex)
    input_value(browser_driver, xpath, value, timeout)
