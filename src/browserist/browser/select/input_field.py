from selenium.webdriver.common.by import By

from ..wait.for_element import wait_for_element


def select_input_field(driver: object, xpath: str) -> None:
    wait_for_element(driver, xpath)
    driver.find_element(By.XPATH, xpath).click()
