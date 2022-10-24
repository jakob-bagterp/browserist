from ....model.browser.base.driver import BrowserDriver
from ....model.viewport.device import DeviceViewportSize
from .size import set_viewport_size


def set_viewport_size_by_device(browser_driver: BrowserDriver, device: DeviceViewportSize) -> None:
    set_viewport_size(browser_driver, device.width, device.height)
