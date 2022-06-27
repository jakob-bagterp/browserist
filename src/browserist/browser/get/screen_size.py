def get_screen_size(driver: object) -> tuple[int, int]:
    width = int(driver.execute_script("return window.innerWidth;"))  # type: ignore
    height = int(driver.execute_script("return window.innerHeight;"))  # type: ignore
    return width, height
