from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from .....exception.timeout import WaitForPageTitleToChangeTimeoutException
from .....model.browser.base.driver import BrowserDriver


def wait_until_page_title_equals(browser_driver: BrowserDriver, page_title: str, timeout: int) -> None:
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(EC.title_is(page_title))  # type: ignore
    except TimeoutException:
        raise WaitForPageTitleToChangeTimeoutException(browser_driver, page_title) from TimeoutException
