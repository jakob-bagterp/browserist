from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ..constant import timeout
from ..exception.element import NoElementFoundException
from ..exception.timeout import WaitForElementTimeoutException

def wait_for_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath)
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath)
