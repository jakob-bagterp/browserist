from ...model.browser.base.driver import BrowserDriver
from ...model.viewport.device import DeviceScreenSize
from .set_size import set_screen_size


def set_screen_size_by_device(browser_driver: BrowserDriver, device: DeviceScreenSize) -> None:
    set_screen_size(browser_driver, device.width, device.height)
