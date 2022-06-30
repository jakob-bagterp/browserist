from ..get.position import get_scroll_position


def check_if_scroll_is_top_of_page(driver: object) -> bool:
    _, y = get_scroll_position(driver)
    return y == 0
