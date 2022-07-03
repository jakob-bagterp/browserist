from ... import helper
from ...model.browser.base.settings import BrowserSettings
from ...model.screenshot import ScreenshotType


def get_screenshot_of_visible_portion(driver: object, settings: BrowserSettings, file_name: str | None = None, destination_dir: str | None = None) -> None:
    destination_dir = helper.screenshot.controller.destination_dir(settings, destination_dir)
    file_name = helper.screenshot.controller.get_file_name(file_name, ScreenshotType.VISIBLE_PORTION)
    helper.screenshot.save(driver, destination_dir, file_name)
