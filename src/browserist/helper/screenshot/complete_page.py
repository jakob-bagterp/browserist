from ... import helper
from ...browser.screenshot.visible_portion import get_screenshot_of_visible_portion
from ...browser.scroll.check_if.is_end_of_page import check_if_scroll_is_end_of_page
from ...browser.scroll.get.position import get_scroll_position
from ...browser.scroll.page.down import scroll_page_down
from ...browser.scroll.page.to_top import scroll_to_top_of_page
from ...browser.scroll.to_position import scroll_to_position
from ...model.browser.base.settings import BrowserSettings
from ...model.screenshot import ScreenshotTempDataHandler


def firefox(driver: object, file_path: str) -> None:
    driver.get_full_page_screenshot_as(file_path)  # type: ignore


def default(driver: object, file_path: str, settings: BrowserSettings, destination_dir: str) -> None:
    def get_screenshot_of_visible_portion_and_scroll_down(driver: object, settings: BrowserSettings, handler: ScreenshotTempDataHandler) -> None:
        get_screenshot_of_visible_portion(driver, settings, handler.get_temp_file_name(), handler.get_temp_dir())
        scroll_page_down(driver)
        handler.next_iteration()

    # Save inital scroll position so we can return to it later.
    x_inital, y_initial = get_scroll_position(driver)

    # Prepare for iteration from the top of the page...
    scroll_to_top_of_page(driver)
    handler = ScreenshotTempDataHandler(destination_dir=destination_dir)

    # ... and take screenshots of the visible portion...
    get_screenshot_of_visible_portion_and_scroll_down(driver, settings, handler)

    # ... until we reach the end of the page.
    while check_if_scroll_is_end_of_page(driver) is not True:
        get_screenshot_of_visible_portion_and_scroll_down(driver, settings, handler)

    # TODO: Consider refactoring to async methods so it runs faster:
    helper.screenshot.merge_images(handler.all_temp_file_paths, file_path)

    # Return to initial scroll position and tidy up temp files.
    scroll_to_position(driver, x_inital, y_initial)
    handler.remove_temp_files()
