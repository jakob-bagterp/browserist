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
    def firefox_get_screenshot_of_complete_page(driver: object, file_path: str) -> None:
        driver.get_full_page_screenshot_as(file_path)  # type: ignore

    def default_get_screenshot_of_complete_page(driver: object, file_name: str, destination_dir: str) -> None:
        x_inital, y_initial = get_scroll_position(driver)
        scroll_to_top_of_page(driver)
        temp_dir = helper.screenshot.controller.mediate_temp_dir(destination_dir)
        temp_file_prefix = helper.screenshot.get_temp_file_prefix_without_iterator_and_file_type()
        all_temp_file_paths: list[str] = []
        i = 1
        while check_if_scroll_is_end_of_page(driver) is not True:
            temp_file_name = f"{temp_file_prefix}_{i}.png"
            get_screenshot_of_visible_portion(driver, settings, temp_file_name, temp_dir)
            scroll_page_down(driver)
            temp_file_path = helper.screenshot.generate_file_path(temp_dir, temp_file_name)
            all_temp_file_paths.append(temp_file_path)
            i += 1
        # TODO: Stitch the temp images together.
        scroll_to_position(driver, x_inital, y_initial)
        helper.file.remove(all_temp_file_paths)

    destination_dir = helper.screenshot.controller.mediate_destination_dir(settings, destination_dir)
    file_name = helper.screenshot.controller.mediate_file_name(file_name, ScreenshotType.COMPLETE_PAGE)
    file_path = helper.screenshot.generate_file_path(destination_dir, file_name)

    match settings.type:
        case BrowserType.FIREFOX:
            firefox_get_screenshot_of_complete_page(driver, file_path)
        case _:
            default_get_screenshot_of_complete_page(driver, file_name, destination_dir)
