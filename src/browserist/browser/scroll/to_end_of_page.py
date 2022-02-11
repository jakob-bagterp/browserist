import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from ...constant import timeout
from ...exception.element import NoElementFoundException

def scroll_to_end_of_page(driver: object):
    try:
        body = driver.find_element_by_tag_name("body") # Select the whole page before pressing any keys...
        body.send_keys(Keys.END) # ... and then simulate pressing End on the keyboard.
        time.sleep(timeout.VERY_SHORT) # Small delay to ensure the view is updated.
    except NoSuchElementException:
        raise NoElementFoundException(driver, "body") from NoSuchElementException
