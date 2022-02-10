from ..wait.for_element import wait_for_element
from ... import helper
from ...constant import timeout

def get_url_from_image(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_src_attribute_of_element(driver: object, xpath: str) -> str:
        return driver.find_element_by_xpath(xpath).get_attribute("src")

    wait_for_element(driver, xpath, timeout)
    return helper.driver.retry_and_get_text_from_element(get_src_attribute_of_element(driver, xpath))
