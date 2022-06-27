from .height import get_screen_height
from .width import get_screen_width


def get_screen_size(driver: object) -> tuple[int, int]:
    width = get_screen_width(driver)
    height = get_screen_height(driver)
    return width, height
