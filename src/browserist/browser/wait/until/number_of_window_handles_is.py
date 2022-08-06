from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from .... import helper
from ....exception.timeout import WaitForWindowTimeoutException
from ....model.browser.base.driver import BrowserDriver


def wait_until_number_of_window_handles_is(browser_driver: BrowserDriver, expected_handles: int, timeout: float) -> None:
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(EC.number_of_windows_to_be(expected_handles))  # type: ignore
    except TimeoutException:
        browser_driver.settings = helper.timeout.set_is_timed_out(browser_driver.settings)
        raise WaitForWindowTimeoutException() from TimeoutException
