from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .....exception.timeout import WaitForUrlTimeoutException
from .....helper.timeout import set_is_timed_out, should_continue
from .....model.browser.base.driver import BrowserDriver


def wait_until_url_contains(browser_driver: BrowserDriver, url_fragment: str, timeout: float) -> None:
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(expected_conditions.url_contains(url_fragment))
    except TimeoutException:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForUrlTimeoutException(browser_driver, url_fragment) from TimeoutException
    except Exception:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForUrlTimeoutException(browser_driver, url_fragment) from Exception
