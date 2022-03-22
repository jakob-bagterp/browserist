def get_window_size(driver: object) -> tuple[int, int]:
    width = int(driver.get_window_size().get("width"))  # type: ignore
    height = int(driver.get_window_size().get("height"))  # type: ignore
    return width, height
