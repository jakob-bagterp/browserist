from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ...constant import timeout
from ...exception.timeout import WaitForWindowTimeoutException


def wait_until_number_of_window_handles_is(driver: object, expected_handles: int, timeout: int = timeout.DEFAULT) -> None:
    try:
        WebDriverWait(driver, timeout).until(EC.number_of_windows_to_be(expected_handles))
    except TimeoutException:
        raise WaitForWindowTimeoutException() from TimeoutException
