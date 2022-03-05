from ...open.url import open_url
from ...wait.until_number_of_window_handles_is import wait_until_number_of_window_handles_is
from ..handle.count import count_window_handles


def open_new_window(driver: object, url: str | None = None) -> None:
    current_number_of_window_handles = count_window_handles(driver)
    driver.switch_to.new_window("window")
    wait_until_number_of_window_handles_is(driver, current_number_of_window_handles + 1)
    if url:
        open_url(driver, url)
