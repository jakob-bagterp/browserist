from ..to_position import scroll_to_position


def scroll_to_top_of_page(driver: object, delay_seconds: float) -> None:
    scroll_to_position(driver, 0, 0, delay_seconds)
