from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from ....exception.timeout import WaitForWindowTimeoutException
from ....helper.timeout import set_is_timed_out, should_continue
from ....model.browser.base.driver import BrowserDriver


def wait_until_number_of_window_handles_is(browser_driver: BrowserDriver, expected_handles: int, timeout: float) -> None:
    if expected_handles < 0:
        raise ValueError("Expected handles must be greater than or equal to 0.")
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(EC.number_of_windows_to_be(expected_handles))  # type: ignore
    except TimeoutException:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForWindowTimeoutException() from TimeoutException
    except Exception:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForWindowTimeoutException() from Exception
