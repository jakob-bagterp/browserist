from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class VivoDevices:
    """Viewport sizes for common Vivo devices.

    Example:
        ```python title="" linenums="1" hl_lines="3 6"
        from browserist import Browser, BrowserSettings, common_devices

        vivo_y20 = common_devices.Vivo.Y20
            settings = BrowserSettings(
            headless=True,
            viewport=vivo_y20)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    Y55S = DeviceViewportSize(360, 640)
    Y20 = DeviceViewportSize(385, 854)
