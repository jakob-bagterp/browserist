from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ...constant import timeout


def check_if_is_element_clickable(driver: object, xpath: str) -> bool:
    try:
        element = WebDriverWait(driver, timeout.VERY_SHORT).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return element is not None
    except (TimeoutException, NoSuchElementException, Exception):
        return False
