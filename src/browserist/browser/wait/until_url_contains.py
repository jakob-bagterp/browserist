from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from ...constant import timeout
from ...exception.timeout import WaitForUrlTimeoutException


def wait_until_url_contains(driver: object, url_fragment: str, timeout: int = timeout.DEFAULT) -> None:
    try:
        WebDriverWait(driver, timeout).until(EC.url_contains(url_fragment))  # type: ignore
    except TimeoutException:
        raise WaitForUrlTimeoutException(driver, url_fragment) from TimeoutException
