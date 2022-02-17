from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def check_if_is_element_visible(driver: object, xpath: str) -> bool:
    try:
        element = driver.find_element(By.XPATH, xpath)
        return element.is_displayed()
    except NoSuchElementException:
        return False
