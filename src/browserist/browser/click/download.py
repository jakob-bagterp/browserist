from ... import factory, helper
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element
from .button import click_button_without_wait


def click_download_button(browser_driver: BrowserDriver, xpath: str, timeout: float, await_download: bool, expected_file_name: str | None, idle_download_timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    if await_download:
        download_dir_entries_before_download = helper.directory.get_entries(browser_driver.settings._download_dir)
    click_button_without_wait(browser_driver, xpath)
    if await_download:
        download_handler = factory.get.download_handler(browser_driver, download_dir_entries_before_download, idle_download_timeout)
        if expected_file_name:
            download_handler.wait_for_expected_file(expected_file_name)
        else:
            download_handler.await_and_get_final_file()
