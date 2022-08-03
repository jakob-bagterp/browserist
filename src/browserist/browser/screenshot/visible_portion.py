from ... import screenshot_helper
from ...model.browser.base.settings import BrowserSettings
from ...model.screenshot import ScreenshotType
from ...model.type.file_png import FilePNG


def get_screenshot_of_visible_portion(driver: object, settings: BrowserSettings, file_name: str | None = None, destination_dir: str | None = None) -> None:
    if file_name is not None:
        file_name = FilePNG(file_name)
    file_name = screenshot_helper.controller.mediate_file_name(file_name, ScreenshotType.VISIBLE_PORTION)
    destination_dir = screenshot_helper.controller.mediate_destination_dir(settings, destination_dir)
    file_path = screenshot_helper.file.get_path(destination_dir, file_name)
    screenshot_helper.save(driver, file_path)
