from ... import helper
from ...model.browser.base.settings import BrowserSettings, BrowserType
from ...model.screenshot import ScreenshotType
from ..scroll.check_if.is_end_of_page import check_if_scroll_is_end_of_page
from ..scroll.get.position import get_scroll_position
from ..scroll.page.down import scroll_page_down
from ..scroll.page.to_top import scroll_to_top_of_page
from ..scroll.to_position import scroll_to_position
from .visible_portion import get_screenshot_of_visible_portion


def get_screenshot_of_complete_page(driver: object, settings: BrowserSettings, file_name: str | None = None, destination_dir: str | None = None) -> None:
    def default_get_screenshot_of_complete_page(driver: object) -> None:
        x_inital, y_initial = get_scroll_position(driver)
        scroll_to_top_of_page(driver)
        while check_if_scroll_is_end_of_page(driver) is not True:
            get_screenshot_of_visible_portion(driver, settings, file_name, destination_dir)
            scroll_page_down(driver)
        scroll_to_position(driver, x_inital, y_initial)

    destination_dir = helper.screenshot.controller.destination_dir(settings, destination_dir)
    file_name = helper.screenshot.controller.file_name(file_name, ScreenshotType.COMPLETE_PAGE)

    match settings.type:
        case BrowserType.FIREFOX:
            pass
        case _:
            default_get_screenshot_of_complete_page(driver)
