from ... import helper
from ...browser.screenshot.visible_portion import get_screenshot_of_visible_portion
from ...browser.scroll.check_if.is_end_of_page import check_if_scroll_is_end_of_page
from ...browser.scroll.get.position import get_scroll_position
from ...browser.scroll.page.down import scroll_page_down
from ...browser.scroll.page.to_top import scroll_to_top_of_page
from ...browser.scroll.to_position import scroll_to_position
from ...model.browser.base.settings import BrowserSettings


def firefox(driver: object, file_path: str) -> None:
    driver.get_full_page_screenshot_as(file_path)  # type: ignore


def default(driver: object, file_path: str, settings: BrowserSettings, destination_dir: str) -> None:
    # Save inital scroll position so we can return to it later.
    x_inital, y_initial = get_scroll_position(driver)

    # Prepare for iteration from the top of the page.
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

    # TODO: Consider refactoring to async methods so it runs faster:
    helper.screenshot.merge_images(all_temp_file_paths, file_path)

    # Return to initial scroll position and tidy up temp files.
    scroll_to_position(driver, x_inital, y_initial)
    helper.file.remove(all_temp_file_paths)
