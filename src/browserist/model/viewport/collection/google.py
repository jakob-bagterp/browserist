from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class GoogleDevices:
    """Viewport sizes for common Google devices.

    Example:
        ```python title=""
        from browserist import Browser, BrowserSettings, common_devices

        settings = BrowserSettings(headless = True)
        nest_hub_max = common_devices.Google.NEST_HUB_MAX

        with Browser(settings) as browser:
            browser.viewport.set.size_by_device(nest_hub_max)
            browser.open.url("https://example.com")
        ```
    """

    PIXEL_5 = DeviceViewportSize(393, 851)
    NEST_HUB = DeviceViewportSize(1024, 600)
    NEST_HUB_MAX = DeviceViewportSize(1280, 800)
