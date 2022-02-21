from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ...constant import timeout
from ...exception.timeout import WaitForPageTitleToChangeTimeoutException


def wait_until_page_title_is(driver: object, page_title: str, timeout: int = timeout.DEFAULT) -> None:
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(page_title))
    except TimeoutException:
        raise WaitForPageTitleToChangeTimeoutException(driver, page_title) from TimeoutException
