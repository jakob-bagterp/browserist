from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from ...constant import timeout
from ..wait.for_element import wait_for_element


def mouse_hover(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    wait_for_element(driver, xpath, timeout)
    element = driver.find_element(By.XPATH, xpath)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
