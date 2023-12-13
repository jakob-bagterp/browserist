from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element
from .button import click_button_without_wait


def click_download_button(browser_driver: BrowserDriver, xpath: str, timeout: float, await_download: bool, expected_file_name: str | None, idle_download_timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    click_button_without_wait(browser_driver, xpath)
    if await_download:
        pass  # TODO: Add watcher flow for file download completion.

    # TODO: Temporary solution. To be updated.
