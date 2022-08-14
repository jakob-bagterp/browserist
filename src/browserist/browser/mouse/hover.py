from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def mouse_hover(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    driver = browser_driver.get_webdriver()
    element = driver.find_element(By.XPATH, xpath)  # type: ignore
    actions = ActionChains(driver)  # type: ignore
    actions.move_to_element(element).perform()  # type: ignore
