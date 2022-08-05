import asyncio

from ... import screenshot_helper
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.type import BrowserType
from ...model.screenshot import ScreenshotType
from ...model.type.file_png import FilePNG


def get_screenshot_of_complete_page(browser_driver: BrowserDriver, file_name: str | None = None, destination_dir: str | None = None, delay_seconds: float = 1) -> None:
    destination_dir = screenshot_helper.controller.mediate_destination_dir(browser_driver.settings, destination_dir)
    if file_name is not None:
        file_name = FilePNG(file_name)
    file_name = screenshot_helper.controller.mediate_file_name(file_name, ScreenshotType.COMPLETE_PAGE)
    destination_file_path = screenshot_helper.file.get_path(destination_dir, file_name)

    match browser_driver.settings.type:
        case BrowserType.FIREFOX:
            screenshot_helper.complete_page.firefox(browser_driver.webdriver, destination_file_path)
        case _:
            asyncio.run(
                screenshot_helper.complete_page.default(
                    browser_driver.webdriver, destination_file_path, destination_dir, delay_seconds)
            )
