from ... import helper
from ...model.browser.base.settings import BrowserSettings
from ...model.type.xpath import XPath
from ..get.element import get_element


def get_screenshot_of_element(driver: object, xpath: str, settings: BrowserSettings, file_name: str | None = None, destination_dir: str | None = None) -> None:
    xpath = XPath(xpath)
    element = get_element(driver, xpath)
    file_name = helper.screenshot.controller.file_name(file_name)
    destination_dir = helper.screenshot.controller.destination_dir(settings, destination_dir)
    helper.screenshot.save_element(element, destination_dir, file_name)
