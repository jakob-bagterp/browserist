from ... import helper

def get_screenshot(driver: object, file_name: str | None = None, destination_dir: str | None = None) -> None:
    if file_name is None:
        file_name = helper.screenshot.default_file_name()
    driver.save_screenshot(f"./{file_name}")
