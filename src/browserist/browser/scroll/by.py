import time

from ...constant import timeout


def scroll_by(driver: object, x: int, y: int, delay: float = timeout.VERY_SHORT) -> None:
    driver.execute_script(f"window.scrollBy({x}, {y});")  # type: ignore
    time.sleep(delay)  # Small delay to ensure the view is updated.
