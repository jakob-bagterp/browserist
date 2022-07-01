import time

from ...constant import timeout


def scroll_by(driver: object, x: int, y: int) -> None:
    driver.execute_script(f"window.scrollBy({x}, {y});")  # type: ignore
    time.sleep(timeout.VERY_SHORT)  # Small delay to ensure the view is updated.
