from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ...constant import timeout
from ...exception.timeout import WaitForUrlTimeoutException

def wait_until_url_contains(driver: object, url: str, timeout: int = timeout.DEFAULT) -> None:
    try:
        WebDriverWait(driver, timeout).until(EC.url_contains(url))
    except TimeoutException:
        raise WaitForUrlTimeoutException(driver, url) from TimeoutException
