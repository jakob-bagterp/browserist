from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class MicrosoftDevices:
    """Viewport sizes for common Microsoft devices.

    Example:
        ```python title="" linenums="1"
        from browserist import Browser, BrowserSettings, common_devices

        surface_pro_7 = common_devices.Microsoft.SURFACE_PRO_7
        settings = BrowserSettings(
            headless = True,
            viewport = surface_pro_7)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    SURFACE_PRO_7 = DeviceViewportSize(912, 1368)
    SURFACE_DUO = DeviceViewportSize(540, 720)
