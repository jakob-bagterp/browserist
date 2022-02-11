import time
from ...constant import timeout

def scroll_to_top_of_page(driver: object) -> None:
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(timeout.VERY_SHORT) # Small delay to ensure the view is updated.
