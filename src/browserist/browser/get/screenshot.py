from ... import helper
from ...model.browser.base.settings import BrowserSettings


def get_screenshot(driver: object, settings: BrowserSettings, file_name: str | None = None, destination_dir: str | None = None) -> None:
    if file_name is None:
        file_name = helper.screenshot.default_file_name()
    if destination_dir is None:
        destination_dir = settings.screenshot_dir
    else:
        destination_dir = helper.directory.ensure_trailing_slash(destination_dir)
        helper.directory.create_if_not_exists(destination_dir)
    driver.save_screenshot(f"{destination_dir}{file_name}")  # type: ignore
