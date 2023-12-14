from ... import helper
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element
from .button import click_button_without_wait


def click_download_button(browser_driver: BrowserDriver, xpath: str, timeout: float, await_download: bool, expected_file_name: str | None, idle_download_timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    if await_download and not expected_file_name:
        download_dir_entries_before_download = helper.directory.get_entries(browser_driver.settings._download_dir)
    click_button_without_wait(browser_driver, xpath)
    if await_download:
        if download_dir_entries_before_download:
            pass
        # TODO: Add watcher flow for file download completion.

    # TODO: Temporary solution. To be updated.
