from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ... import constant
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException
from ...helper.timeout import set_is_timed_out, should_continue
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath


def wait_for_element(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    if timeout == constant.timeout.BYPASS:
        return
    try:
        driver = browser_driver.get_webdriver()
        WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForElementTimeoutException(browser_driver, xpath) from TimeoutException
    except NoSuchElementException:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise NoElementFoundException(browser_driver, xpath) from NoSuchElementException
    except Exception:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise WaitForElementTimeoutException(browser_driver, xpath) from Exception
