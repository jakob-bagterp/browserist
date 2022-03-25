from selenium.webdriver.common.by import By

from ..wait.for_element import wait_for_element


def switch_to_iframe(driver: object, xpath: str) -> None:
    wait_for_element(driver, xpath)
    iframe_element = driver.find_element(By.XPATH, xpath)  # type: ignore
    driver.switch_to.frame(iframe_element)  # type: ignore
