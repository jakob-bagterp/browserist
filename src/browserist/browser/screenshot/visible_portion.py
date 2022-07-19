from ... import helper
from ...model.browser.base.settings import BrowserSettings
from ...model.screenshot import ScreenshotType


def get_screenshot_of_visible_portion(driver: object, settings: BrowserSettings, file_name: str | None = None, destination_dir: str | None = None) -> None:
    file_name = helper.screenshot.controller.mediate_file_name(file_name, ScreenshotType.VISIBLE_PORTION)
    destination_dir = helper.screenshot.controller.mediate_destination_dir(settings, destination_dir)
    file_path = helper.screenshot.file.get_path(destination_dir, file_name)
    helper.screenshot.save(driver, file_path)
