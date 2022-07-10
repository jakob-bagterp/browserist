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
    def merge_images(all_temp_file_paths: list[str], save_file_path: str) -> None:
        merged_image = all_temp_file_paths[0]
        if len(all_temp_file_paths) > 1:
            for file_path in all_temp_file_paths[1:]:
                image_add = helper.image.open(file_path)
                merged_image = helper.image.merge_vertically(merged_image, image_add)
        helper.image.save(merged_image, save_file_path)

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
    # TODO: Consider refactoring to async methods so it runs faster:
    merge_images(all_temp_file_paths, file_path)
    scroll_to_position(driver, x_inital, y_initial)
    helper.file.remove(all_temp_file_paths)
