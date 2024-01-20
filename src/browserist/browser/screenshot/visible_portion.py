from pathlib import Path

from ... import helper_screenshot
from ...model.browser.base.driver import BrowserDriver
from ...model.screenshot import ScreenshotType
from ...model.type.file_png import FilePNG


def get_screenshot_of_visible_portion(browser_driver: BrowserDriver, file_name: str | None = None, destination_dir: str | Path | None = None) -> None:
    if file_name is not None:
        file_name = FilePNG(file_name)
    file_name = helper_screenshot.controller.mediate_file_name(browser_driver, file_name, ScreenshotType.VISIBLE_PORTION)
    destination_dir = helper_screenshot.controller.mediate_destination_dir(browser_driver.settings, destination_dir)
    file_path = helper_screenshot.file.get_path(file_name, destination_dir)
    helper_screenshot.save(browser_driver, file_path)
