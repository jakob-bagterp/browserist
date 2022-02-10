from selenium.common.exceptions import NoSuchElementException

def check_if_is_element_visible(driver: object, xpath: str) -> bool:
    try:
        element = driver.find_element_by_xpath(xpath)
        return element.is_displayed()
    except NoSuchElementException:
        return False
