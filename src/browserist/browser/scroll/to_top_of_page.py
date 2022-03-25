from .to_position import scroll_to_position


def scroll_to_top_of_page(driver: object) -> None:
    scroll_to_position(driver, 0, 0)
