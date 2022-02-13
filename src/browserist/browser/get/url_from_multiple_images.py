from typing import List
from ..wait.for_element import wait_for_element
from ...constant import timeout

def get_url_from_multiple_images(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements_by_xpath(xpath)
    return [element.get_attribute("src") for element in elements]