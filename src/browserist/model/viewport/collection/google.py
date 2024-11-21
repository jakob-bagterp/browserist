from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class GoogleDevices:
    """Viewport sizes for common Google devices.

    Example:
        ```python title="" linenums="1" hl_lines="3 6"
        from browserist import Browser, BrowserSettings, common_devices

        nest_hub_max = common_devices.Google.NEST_HUB_MAX
        settings = BrowserSettings(
            headless=True,
            viewport=nest_hub_max)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    PIXEL_5 = DeviceViewportSize(393, 851)

    PIXEL_4A = DeviceViewportSize(393, 851)
    PIXEL_4_XL = DeviceViewportSize(412, 869)
    PIXEL_4 = DeviceViewportSize(393, 830)

    PIXEL_3A_XL = DeviceViewportSize(412, 823)
    PIXEL_3A = DeviceViewportSize(393, 808)
    PIXEL_3_XL = DeviceViewportSize(412, 846)
    PIXEL_3 = DeviceViewportSize(393, 786)

    PIXEL_2_XL = DeviceViewportSize(412, 823)
    PIXEL_2 = DeviceViewportSize(412, 732)

    PIXEL_1_XL = DeviceViewportSize(412, 732)
    PIXEL_1 = DeviceViewportSize(412, 732)

    NEST_HUB = DeviceViewportSize(1024, 600)
    NEST_HUB_MAX = DeviceViewportSize(1280, 800)
