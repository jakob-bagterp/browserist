import time


def scroll_by(driver: object, x: int, y: int, delay_seconds: float) -> None:
    driver.execute_script(f"window.scrollBy({x}, {y});")  # type: ignore
    time.sleep(delay_seconds)  # Small delay to ensure that the screen is updated after scroll.
