def get_screen_width(driver: object) -> int:
    return int(driver.execute_script("return window.innerWidth;"))  # type: ignore
