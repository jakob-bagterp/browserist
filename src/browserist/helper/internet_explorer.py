from winreg import CloseKey, OpenKey, SetValueEx, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.type import BrowserType

def disable_images(browser_driver: BrowserDriver) -> None:
    if browser_driver.settings.type is BrowserType.INTERNET_EXPLORER:
        key = OpenKey(HKEY_CURRENT_USER, r"Software\Microsoft\Internet Explorer\Main", 0, KEY_ALL_ACCESS)
        SetValueEx(key, "Display Inline Images", 0, REG_SZ, "no")
        CloseKey(key)
