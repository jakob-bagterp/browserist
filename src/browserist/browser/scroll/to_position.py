import time

from ...constant import timeout


def scroll_to_position(driver: object, x: int, y: int, delay: float = timeout.VERY_SHORT) -> None:
    driver.execute_script(f"window.scrollTo({x}, {y});")  # type: ignore
    time.sleep(delay)  # Small delay in seconds to ensure the view is updated.
