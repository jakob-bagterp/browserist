from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from ..... import helper
from .....exception.timeout import WaitForPageTitleToChangeTimeoutException
from .....model.browser.base.driver import BrowserDriver


def wait_until_page_title_equals(browser_driver: BrowserDriver, page_title: str, timeout: float) -> None:
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(EC.title_is(page_title))  # type: ignore
    except TimeoutException:
        browser_driver.settings = helper.timeout.set_is_timed_out(browser_driver.settings)
        raise WaitForPageTitleToChangeTimeoutException(browser_driver, page_title) from TimeoutException
