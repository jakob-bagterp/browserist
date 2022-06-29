import time

from ...constant import timeout
from ..get.screen.height import get_screen_height


def scroll_page_up(driver: object) -> None:
    screen_height = get_screen_height(driver)
    driver.execute_script(f"window.scrollBy(0, -{screen_height + 1});")  # type: ignore
    time.sleep(timeout.VERY_SHORT)  # Small delay to ensure the view is updated.
