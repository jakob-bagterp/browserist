from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class MicrosoftDevices:
    """Viewport sizes for common Microsoft devices.

    Example:
        ```python title="" linenums="1" hl_lines="3 6"
        from browserist import Browser, BrowserSettings, common_devices

        surface_pro_7 = common_devices.Microsoft.SURFACE_PRO_7
        settings = BrowserSettings(
            headless=True,
            viewport=surface_pro_7)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    SURFACE_PRO_X = DeviceViewportSize(960, 1440)
    SURFACE_PRO_7 = DeviceViewportSize(912, 1368)
    SURFACE_PRO_6 = DeviceViewportSize(912, 1368)
    SURFACE_PRO_5 = DeviceViewportSize(912, 1368)
    SURFACE_PRO_4 = DeviceViewportSize(912, 1368)
    SURFACE_PRO_3 = DeviceViewportSize(960, 1440)
    SURFACE_PRO_2 = DeviceViewportSize(720, 1280)
    SURFACE_PRO_1 = DeviceViewportSize(720, 1280)

    SURFACE_3 = DeviceViewportSize(720, 1280)
    SURFACE_2 = DeviceViewportSize(720, 1280)
    SURFACE_1 = DeviceViewportSize(768, 1366)

    SURFACE_DUO = DeviceViewportSize(540, 720)
