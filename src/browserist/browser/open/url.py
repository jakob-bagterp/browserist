from ...model.type.url import URL


def open_url(driver: object, url: str) -> None:
    url = URL(url)
    driver.get(url)  # type: ignore
