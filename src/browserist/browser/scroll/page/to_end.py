import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ....constant import timeout
from ....exception.element import NoElementFoundException


def scroll_to_end_of_page(driver: object, delay: float = timeout.VERY_SHORT) -> None:
    try:
        # Select the whole page before pressing any keys...
        body_element = driver.find_element(By.TAG_NAME, "body")  # type: ignore
        # ... and then simulate pressing End on the keyboard:
        body_element.send_keys(Keys.END)
        time.sleep(delay)  # Small delay in seconds to ensure the view is updated.
    except NoSuchElementException:
        raise NoElementFoundException(driver, "body") from NoSuchElementException
