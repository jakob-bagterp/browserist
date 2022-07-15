def get_screen_height(driver: object) -> int:
    return int(driver.execute_script("return window.innerHeight;"))  # type: ignore
