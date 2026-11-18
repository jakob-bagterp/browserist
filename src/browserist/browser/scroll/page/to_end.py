from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from ....exception.element import NoElementFoundException
from ....exception.scroll import ScrollException
from ....helper.timeout import set_is_timed_out, should_continue
from ....model.browser.base.driver import BrowserDriver
from ..get.position import get_scroll_position
from ..get.total_height import get_total_scroll_height
from ..to_position import scroll_to_position


def scroll_to_end_of_page(browser_driver: BrowserDriver, delay_seconds: float) -> None:
    try:
        browser_driver.get_webdriver().find_element(By.TAG_NAME, "body")
        x, _ = get_scroll_position(browser_driver)
        y_end = get_total_scroll_height(browser_driver)
        scroll_to_position(browser_driver, x, y_end, delay_seconds)
    except NoSuchElementException:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise NoElementFoundException(browser_driver, "body") from NoSuchElementException
    except Exception:
        browser_driver.settings = set_is_timed_out(browser_driver.settings)
        if not should_continue(browser_driver.settings):
            raise ScrollException() from Exception
