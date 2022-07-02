from ... import helper
from ...model.browser.base.settings import BrowserSettings
from ..screenshot import default_file_name


def file_name(file_name: str | None) -> str:
    return default_file_name() if file_name is None else file_name


def destination_dir(settings: BrowserSettings, destination_dir: str | None = None) -> str:
    if destination_dir is None:
        return settings.screenshot_dir
    helper.directory.create_if_not_exists(destination_dir)
    return helper.directory.ensure_trailing_slash(destination_dir)
