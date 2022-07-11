from ... import helper
from ...model.browser.base.settings import BrowserSettings
from ...model.browser.base.type import BrowserType
from ...model.screenshot import ScreenshotType


def get_screenshot_of_complete_page(driver: object, settings: BrowserSettings, file_name: str | None = None, destination_dir: str | None = None) -> None:
    destination_dir = helper.screenshot.controller.mediate_destination_dir(settings, destination_dir)
    file_name = helper.screenshot.controller.mediate_file_name(file_name, ScreenshotType.COMPLETE_PAGE)
    file_path = helper.screenshot.file.get_path(destination_dir, file_name)

    match settings.type:
        case BrowserType.FIREFOX:
            helper.screenshot.complete_page.firefox(driver, file_path)
        case _:
            helper.screenshot.complete_page.default(driver, file_path, settings, destination_dir)
