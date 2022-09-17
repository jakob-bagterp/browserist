from ...model.browser.base.driver import BrowserDriver
from ...model.viewport.device import DeviceViewport
from .set_size import set_screen_size


def set_screen_size_by_device(browser_driver: BrowserDriver, device: DeviceViewport) -> None:
    set_screen_size(browser_driver, device.width, device.height)
