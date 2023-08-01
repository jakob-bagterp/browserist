from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class GoogleDevices:
    """Viewport sizes for common Google devices.

    Example:
        ```python title="" linenums="1"
        from browserist import Browser, BrowserSettings, common_devices

        nest_hub_max = common_devices.Google.NEST_HUB_MAX
        settings = BrowserSettings(
            headless = True,
            viewport = nest_hub_max)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    PIXEL_5 = DeviceViewportSize(393, 851)
    NEST_HUB = DeviceViewportSize(1024, 600)
    NEST_HUB_MAX = DeviceViewportSize(1280, 800)
