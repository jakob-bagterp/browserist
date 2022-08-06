from .. import constant, helper, helper_screenshot
from ..model.browser.base.settings import BrowserSettings
from ..model.screenshot import ScreenshotType


def mediate_file_name(file_name: str | None, screenshot_type: ScreenshotType | None = None) -> str:
    return helper_screenshot.file.get_default_name(screenshot_type) if file_name is None else file_name


def mediate_destination_dir(settings: BrowserSettings, destination_dir: str | None = None) -> str:
    if destination_dir is None:
        return settings.screenshot_dir
    helper.directory.create_if_not_exists(destination_dir)
    return helper.directory.ensure_trailing_slash(destination_dir)


def mediate_temp_dir(destination_dir: str) -> str:
    """As the temporary directory will be a sub directory to the destination, this assumes that the destination directory has been defined by the controller."""

    destination_dir = helper.directory.ensure_trailing_slash(destination_dir)
    temp_dir = f"{destination_dir}{constant.screenshot.TEMP_DIR}/"
    helper.directory.create_if_not_exists(temp_dir)
    return temp_dir
