from selenium.webdriver.common.action_chains import ActionChains
from ..wait.for_element import wait_for_element
from ...constant import timeout

def hover_mouse_on_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    wait_for_element(driver, xpath, timeout)
    element = driver.find_element_by_xpath(xpath)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
