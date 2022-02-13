def get_window_size(driver: object) -> tuple[int, int]:
    width = driver.get_window_size().get("width")
    height = driver.get_window_size().get("height")
    return width, height
