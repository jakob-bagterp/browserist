def get_scroll_position(driver: object) -> tuple[int, int]:
    x = int(driver.execute_script("return window.pageXOffset;"))  # type: ignore
    y = int(driver.execute_script("return window.pageYOffset;"))  # type: ignore
    return x, y
