from pathlib import Path

from ... import helper_screenshot
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.screenshot import ScreenshotType
from ...model.type.file_png import FilePNG
from ...model.type.xpath import XPath
from ..get.element import get_element


def get_screenshot_of_element(browser_driver: BrowserDriver, xpath: str, file_name: str | None = None, destination_dir: str | Path | None = None) -> None:
    xpath = XPath(xpath)
    if file_name is not None:
        file_name = FilePNG(file_name)
    file_name = helper_screenshot.controller.mediate_file_name(browser_driver, file_name, ScreenshotType.ELEMENT)
    destination_dir = helper_screenshot.controller.mediate_destination_dir(browser_driver.settings, destination_dir)
    file_path = helper_screenshot.file.get_path(file_name, destination_dir)
    element = get_element(browser_driver, xpath, timeout.DEFAULT)
    helper_screenshot.save_element(element, file_path)
