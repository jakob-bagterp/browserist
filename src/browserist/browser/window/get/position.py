def get_window_position(driver: object) -> tuple[int, int]:
    x = int(driver.get_window_position().get("x"))  # type: ignore
    y = int(driver.get_window_position().get("y"))  # type: ignore
    return x, y
