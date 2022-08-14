from ....model.browser.base.driver import BrowserDriver
from ..by import scroll_by
from ..get.position import get_scroll_position

Y_TEST_DISTANCE = 1


def check_if_scroll_is_end_of_page(browser_driver: BrowserDriver) -> bool:
    # Let's assume that we can't scroll further than the end of the page...
    _, y_before = get_scroll_position(browser_driver)
    # ... and so scrolling down should yield the same position as the initial one.
    scroll_by(browser_driver, 0, Y_TEST_DISTANCE, delay_seconds=0)
    _, y_after = get_scroll_position(browser_driver)
    # Remember to reset the scroll position to initial position:
    scroll_by(browser_driver, 0, -Y_TEST_DISTANCE, delay_seconds=0)
    return y_before == y_after
