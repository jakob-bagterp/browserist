from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ..wait.for_element import wait_for_element
from ...constant import timeout
from ...exception.element import NoElementDimensionsFoundException
from ...exception.timeout import WaitForElementTimeoutException

def get_dimensions_of_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> tuple[int, int]:
    wait_for_element(driver, xpath, timeout)
    try:
        dimensions = driver.find_element_by_xpath(xpath).size # Returns dictionary object, e.g. {'height': 598, 'width': 479}.
        return dimensions.get("width"), dimensions.get("height")
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementDimensionsFoundException(driver, xpath) from NoSuchElementException
