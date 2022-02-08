from selenium.common.exceptions import NoSuchElementException

def check_if_does_element_exist(driver: object, xpath: str) -> bool:
    try:
        element = driver.find_element_by_xpath(xpath)
        return element is not None
    except NoSuchElementException:
        return False
