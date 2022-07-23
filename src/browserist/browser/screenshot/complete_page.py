import asyncio

from ... import helper
from ...model.browser.base.settings import BrowserSettings
from ...model.browser.base.type import BrowserType
from ...model.screenshot import ScreenshotType
from ...model.type.file_png import FilePNG


def get_screenshot_of_complete_page(driver: object, settings: BrowserSettings, file_name: str | None = None, destination_dir: str | None = None, delay_seconds: float = 1) -> None:
    destination_dir = helper.screenshot.controller.mediate_destination_dir(settings, destination_dir)
    if file_name is not None:
        file_name = FilePNG(file_name)
    file_name = helper.screenshot.controller.mediate_file_name(file_name, ScreenshotType.COMPLETE_PAGE)
    destination_file_path = helper.screenshot.file.get_path(destination_dir, file_name)

    match settings.type:
        case BrowserType.FIREFOX:
            helper.screenshot.complete_page.firefox(driver, destination_file_path)
        case _:
            asyncio.run(
                helper.screenshot.complete_page.default(driver, destination_file_path, destination_dir, delay_seconds)
            )
