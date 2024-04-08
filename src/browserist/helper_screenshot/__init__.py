__all__ = ["complete_page", "controller", "file", "save", "save_element", "merge_two_images_without_save"]


from PIL.Image import Image as ImageType
from selenium.webdriver.remote.webelement import WebElement

from .. import helper
from ..model.browser.base.driver import BrowserDriver
from . import complete_page, controller, file


def save(browser_driver: BrowserDriver, file_path: str) -> None:
    """Take screenshot of visible portion. Reference: https://www.selenium.dev/documentation/webdriver/browser/windows/#takescreenshot"""

    driver = browser_driver.get_webdriver()
    driver.save_screenshot(file_path)


def save_element(element: WebElement, file_path: str) -> None:
    """Take screenshot of element. Reference: https://www.selenium.dev/documentation/webdriver/browser/windows/#takeelementscreenshot"""

    element.screenshot(file_path)


def merge_two_images_without_save(image_1: ImageType, image_2: ImageType) -> ImageType:
    return helper.image.merge_vertically(image_1, image_2)
