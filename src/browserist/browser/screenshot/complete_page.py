import asyncio

from ... import helper_screenshot
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.type import BrowserType
from ...model.screenshot import ScreenshotType
from ...model.type.file_png import FilePNG


def get_screenshot_of_complete_page(browser_driver: BrowserDriver, file_name: str | None = None, destination_dir: str | None = None, delay_seconds: float = 1) -> None:
    destination_dir = helper_screenshot.controller.mediate_destination_dir(browser_driver.settings, destination_dir)
    if file_name is not None:
        file_name = FilePNG(file_name)
    file_name = helper_screenshot.controller.mediate_file_name(file_name, ScreenshotType.COMPLETE_PAGE)
    destination_file_path = helper_screenshot.file.get_path(file_name, destination_dir)

    match browser_driver.settings.type:
        case BrowserType.FIREFOX:
            helper_screenshot.complete_page.firefox(browser_driver, destination_file_path)
        case _:
            asyncio.run(
                helper_screenshot.complete_page.default(
                    browser_driver, destination_file_path, destination_dir, delay_seconds)
            )
