from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class MicrosoftDevices:
    """Viewport sizes for common Microsoft devices.

    Example:
        ```python title=""
        from browserist import Browser, BrowserSettings, common_devices

        settings = BrowserSettings(headless = True)
        surface_pro_7 = common_devices.Microsoft.SURFACE_PRO_7

        with Browser(settings) as browser:
            browser.viewport.set.size_by_device(surface_pro_7)
            browser.open.url("https://example.com")
        ```
    """

    SURFACE_PRO_7 = DeviceViewportSize(912, 1368)
    SURFACE_DUO = DeviceViewportSize(540, 720)
