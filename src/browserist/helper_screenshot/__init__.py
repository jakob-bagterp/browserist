__all__ = ["complete_page", "controller", "file", "save", "save_element"]


from .. import helper
from ..model.browser.base.driver import BrowserDriver
from . import complete_page, controller, file


def save(browser_driver: BrowserDriver, file_path: str) -> None:
    """Take screenshot of visible portion. Reference: https://www.selenium.dev/documentation/webdriver/browser/windows/#takescreenshot"""

    driver = browser_driver.get_webdriver()
    driver.save_screenshot(file_path)  # type: ignore


def save_element(element: object, file_path: str) -> None:
    """Take screenshot of element. Reference: https://www.selenium.dev/documentation/webdriver/browser/windows/#takeelementscreenshot"""

    element.screenshot(file_path)  # type: ignore


def merge_images(all_temp_file_paths: list[str], save_file_path: str) -> None:
    if not all_temp_file_paths:
        return
    merged_image = helper.image.open(all_temp_file_paths[0])
    if len(all_temp_file_paths) > 1:
        for file_path in all_temp_file_paths[1:]:
            image_add = helper.image.open(file_path)
            merged_image = helper.image.merge_vertically(merged_image, image_add)
    helper.image.save(merged_image, save_file_path)
