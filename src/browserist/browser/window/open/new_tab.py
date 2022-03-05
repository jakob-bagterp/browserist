from ...wait.until_number_of_window_handles_is import wait_until_number_of_window_handles_is
from ..handle.count import count_window_handles


def open_new_tab(driver: object, url: str | None = None) -> None:
    current_number_of_window_handles = count_window_handles(driver)
    if url:
        # To ensure support across browsers, use JavaScript rather than CTRL + K keys combination.
        driver.execute_script(f"window.open('{url}', '_blank');")
    else:
        driver.switch_to.new_window("tab")
    wait_until_number_of_window_handles_is(driver, current_number_of_window_handles + 1)
