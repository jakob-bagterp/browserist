from ...open.url import open_url


def open_new_window(driver: object, url: str | None = None) -> None:
    driver.switch_to.new_window("window")
    if url:
        open_url(driver, url)
