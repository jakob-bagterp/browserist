from ... import helper
from ...model.browser.base.settings import BrowserSettings
from ...model.screenshot import ScreenshotType
from ...model.type.file_png import FilePNG
from ...model.type.xpath import XPath
from ..get.element import get_element


def get_screenshot_of_element(driver: object, xpath: str, settings: BrowserSettings, file_name: str | None = None, destination_dir: str | None = None) -> None:
    xpath = XPath(xpath)
    if file_name is not None:
        file_name = FilePNG(file_name)
    file_name = helper.screenshot.controller.mediate_file_name(file_name, ScreenshotType.ELEMENT)
    destination_dir = helper.screenshot.controller.mediate_destination_dir(settings, destination_dir)
    file_path = helper.screenshot.file.get_path(destination_dir, file_name)
    element = get_element(driver, xpath)
    helper.screenshot.save_element(element, file_path)
