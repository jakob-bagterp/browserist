from pathlib import Path

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element
from .button import click_button_without_wait


def click_download_button_and_get_file_path(browser_driver: BrowserDriver, xpath: str, timeout: float) -> Path:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    click_button_without_wait(browser_driver, xpath)

    return Path(browser_driver.settings._download_dir)  # TODO: Temporary solution. To be updated.
