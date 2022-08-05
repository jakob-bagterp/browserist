from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from .....exception.timeout import WaitForUrlTimeoutException
from .....model.browser.base.driver import BrowserDriver


def wait_until_url_contains(browser_driver: BrowserDriver, url_fragment: str, timeout: int) -> None:
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(EC.url_contains(url_fragment))  # type: ignore
    except TimeoutException:
        raise WaitForUrlTimeoutException(browser_driver, url_fragment) from TimeoutException
