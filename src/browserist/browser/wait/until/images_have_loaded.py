from selenium.webdriver.common.by import By

from .... import helper, helper_iteration
from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ..for_element import wait_for_element


def wait_until_images_have_loaded(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    def are_all_images_loaded(browser_driver: BrowserDriver, elements: list[object]) -> bool:
        return all(helper.image.is_element_loaded(browser_driver.webdriver, element) is not False for element in elements)

    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    driver = browser_driver.get_webdriver()
    elements: list[object] = driver.find_elements(By.XPATH, xpath)  # type: ignore
    helper_iteration.retry.until_condition_is_true(
        browser_driver, elements, func=are_all_images_loaded, timeout=timeout)
