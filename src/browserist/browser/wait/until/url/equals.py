from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .....exception.timeout import WaitForUrlTimeoutException
from .....helper.timeout import set_is_timed_out, should_continue
from .....model.browser.base.driver import BrowserDriver
from .....model.type.url import URL


def wait_until_url_equals(browser_driver: BrowserDriver, url: str, timeout: float) -> None:
    url = URL(url)
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(expected_conditions.url_matches(url))
    except TimeoutException:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForUrlTimeoutException(browser_driver, url) from TimeoutException
    except Exception:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForUrlTimeoutException(browser_driver, url) from Exception
