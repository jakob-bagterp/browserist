from .... import helper
from ....exception.scroll import PageValueError
from ....model.browser.base.driver import BrowserDriver
from ...viewport.get.height import get_viewport_height
from ..by import scroll_by
from ..get.position import get_scroll_position


def scroll_page_down(browser_driver: BrowserDriver, pages: int, delay_seconds: float) -> None:
    def is_end_of_page(y_position_before_scroll: int, y_position_after_scroll: int) -> bool:
        return y_position_before_scroll == y_position_after_scroll

    if not helper.scroll.is_valid_page_number(pages):
        raise PageValueError(pages)

    screen_height = get_viewport_height(browser_driver)
    y_scroll_pixels = screen_height + 1
    if pages == 1:
        scroll_by(browser_driver, 0, y_scroll_pixels, delay_seconds)
        return
    for page in range(1, pages + 1):
        _, y_position_before_scroll = get_scroll_position(browser_driver)
        delay = 0 if page < pages else delay_seconds  # Only add delay on the last page scroll.
        scroll_by(browser_driver, 0, y_scroll_pixels, delay)
        _, y_position_after_scroll = get_scroll_position(browser_driver)
        if pages > 1 and is_end_of_page(y_position_before_scroll, y_position_after_scroll):
            break
