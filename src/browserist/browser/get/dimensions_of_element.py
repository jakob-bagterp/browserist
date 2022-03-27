from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from ...constant import timeout
from ...exception.element import NoElementDimensionsFoundException
from ...exception.timeout import WaitForElementTimeoutException
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_dimensions_of_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> tuple[int, int]:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    try:
        # Returns dictionary object, e.g. {'height': 598, 'width': 479}:
        dimensions: dict[str, int] = driver.find_element(By.XPATH, xpath).size  # type: ignore
        return dimensions.get("width") or 0, dimensions.get("height") or 0
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementDimensionsFoundException(driver, xpath) from NoSuchElementException
