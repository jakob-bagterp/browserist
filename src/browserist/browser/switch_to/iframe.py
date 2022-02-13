from ..wait.for_element import wait_for_element

def switch_to_iframe(driver: object, xpath: str) -> None:
    wait_for_element(driver, xpath)
    iframe = driver.find_element_by_xpath(xpath)
    driver.switch_to.frame(iframe)
