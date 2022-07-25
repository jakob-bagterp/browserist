from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from ...model.browser.base.settings import BrowserSettings
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def mouse_hover(driver: object, settings: BrowserSettings, xpath: str, timeout: int) -> None:
    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    element = driver.find_element(By.XPATH, xpath)  # type: ignore
    actions = ActionChains(driver)  # type: ignore
    actions.move_to_element(element).perform()  # type: ignore
