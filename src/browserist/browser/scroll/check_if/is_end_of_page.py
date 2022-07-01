from ..by import scroll_by
from ..get.position import get_scroll_position

Y_TEST_DISTANCE = 1


def check_if_scroll_is_end_of_page(driver: object) -> bool:
    # Let's assume that we can't scroll further than the end of the page...
    _, y_initial = get_scroll_position(driver)
    # ... and so scrolling down should yield the same position as the initial one.
    scroll_by(driver, 0, Y_TEST_DISTANCE)
    _, y_after = get_scroll_position(driver)
    # Remember to reset the scroll position to initial position:
    scroll_by(driver, 0, -Y_TEST_DISTANCE)
    return y_initial == y_after
