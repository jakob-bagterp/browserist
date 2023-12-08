from ..helper import operating_system

if operating_system.is_windows():
    from winreg import CloseKey, OpenKey, SetValueEx, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ

from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.type import BrowserType


def set_internet_explorer_options_in_registry(browser_driver: BrowserDriver, value_name: str, value: str) -> None:
    if browser_driver.settings.type is BrowserType.INTERNET_EXPLORER and operating_system.is_windows():
        key = OpenKey(HKEY_CURRENT_USER, r"Software\Microsoft\Internet Explorer\Main", 0, KEY_ALL_ACCESS)
        SetValueEx(key, value_name, 0, REG_SZ, value)
        CloseKey(key)


def set_image_loading(browser_driver: BrowserDriver, load_images: bool = True) -> None:
    set_internet_explorer_options_in_registry(browser_driver, "Display Inline Images", "yes" if load_images else "no")


def disable_images(browser_driver: BrowserDriver) -> None:
    set_image_loading(browser_driver, load_images=False)


def enable_images(browser_driver: BrowserDriver) -> None:
    set_image_loading(browser_driver, load_images=True)


def set_download_directory(browser_driver: BrowserDriver) -> None:
    if browser_driver.settings._download_dir is not None:
        set_internet_explorer_options_in_registry(browser_driver, "Default Download Directory", browser_driver.settings._download_dir)
