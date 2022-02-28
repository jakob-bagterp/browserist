def get_scroll_position(driver: object) -> tuple[int, int]:
    x = int(driver.execute_script("return window.pageXOffset;"))
    y = int(driver.execute_script("return window.pageYOffset;"))
    return x, y
