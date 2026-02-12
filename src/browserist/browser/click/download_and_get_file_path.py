from pathlib import Path

from ... import factory, helper
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element
from .button import click_button_without_wait


def click_download_button_and_get_file_path(
    browser_driver: BrowserDriver, xpath: str, timeout: float, idle_download_timeout: float
) -> Path:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    download_dir_entries_before_download = helper.directory.get_entries(browser_driver.settings._download_dir)
    click_button_without_wait(browser_driver, xpath)
    download_handler = factory.get.download_handler(
        browser_driver, download_dir_entries_before_download, idle_download_timeout
    )
    return download_handler.await_and_get_final_file()
