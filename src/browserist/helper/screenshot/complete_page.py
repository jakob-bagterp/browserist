def firefox(driver: object, file_path: str) -> None:
    driver.get_full_page_screenshot_as(file_path)  # type: ignore
