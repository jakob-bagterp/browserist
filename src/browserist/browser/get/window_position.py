def get_window_position(driver: object) -> tuple[int, int]:
    x = driver.get_window_position().get("x")
    y = driver.get_window_position().get("y")
    return x, y
