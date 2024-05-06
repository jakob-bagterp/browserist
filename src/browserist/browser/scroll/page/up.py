from .... import helper
from ....exception.scroll import PageValueError
from ....model.browser.base.driver import BrowserDriver
from ...viewport.get.height import get_viewport_height
from ..by import scroll_by
from ..check_if.is_top_of_page import check_if_scroll_is_top_of_page


def scroll_page_up(browser_driver: BrowserDriver, pages: int, delay_seconds: float) -> None:
    if not helper.scroll.is_valid_page_number(pages):
        raise PageValueError(pages)

    screen_height = get_viewport_height(browser_driver)
    y_scroll_pixels = -(screen_height + 1)
    if pages == 1:
        scroll_by(browser_driver, 0, y_scroll_pixels, delay_seconds)
        return
    for page in range(1, pages + 1):
        if check_if_scroll_is_top_of_page(browser_driver):
            break
        delay = 0 if page < pages else delay_seconds  # Only add delay on the last page scroll.
        scroll_by(browser_driver, 0, y_scroll_pixels, delay)
