from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from .....exception.timeout import WaitForUrlTimeoutException
from .....model.browser.base.driver import BrowserDriver
from .....model.type.url import URL


def wait_until_url_equals(browser_driver: BrowserDriver, url: str, timeout: int) -> None:
    url = URL(url)
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(EC.url_matches(url))  # type: ignore
    except TimeoutException:
        raise WaitForUrlTimeoutException(browser_driver, url) from TimeoutException
