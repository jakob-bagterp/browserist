import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ....exception.element import NoElementFoundException
from ....model.browser.base.driver import BrowserDriver


def scroll_to_end_of_page(browser_driver: BrowserDriver, delay_seconds: float) -> None:
    try:
        driver = browser_driver.get_webdriver()
        # Select the whole page before pressing any keys...
        body_element = driver.find_element(By.TAG_NAME, "body")  # type: ignore
        # ... and then simulate pressing End on the keyboard:
        body_element.send_keys(Keys.END)
        time.sleep(delay_seconds)  # Small delay to ensure that the screen is updated after scroll.
    except NoSuchElementException:
        raise NoElementFoundException(browser_driver, "body") from NoSuchElementException
