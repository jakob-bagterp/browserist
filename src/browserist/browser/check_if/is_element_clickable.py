from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ..wait.for_element import wait_for_element
from ...constant import interval, timeout

def check_if_is_element_clickable(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> bool:
    wait_for_element(driver, xpath, timeout)
    try:
        element = WebDriverWait(driver, interval.DEFAULT).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return element is not None
    except TimeoutException:
        return False
    except NoSuchElementException:
        return False
