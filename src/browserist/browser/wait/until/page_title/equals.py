from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .....exception.timeout import WaitForPageTitleToChangeTimeoutException
from .....helper.timeout import set_is_timed_out, should_continue
from .....model.browser.base.driver import BrowserDriver


def wait_until_page_title_equals(browser_driver: BrowserDriver, page_title: str, timeout: float) -> None:
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(expected_conditions.title_is(page_title))
    except TimeoutException:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForPageTitleToChangeTimeoutException(browser_driver, page_title) from TimeoutException
    except Exception:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForPageTitleToChangeTimeoutException(browser_driver, page_title) from Exception
