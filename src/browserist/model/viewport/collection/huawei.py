from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class HuaweiDevices:
    """Viewport sizes for common Huawei devices.

    Example:
        ```python title="" linenums="1" hl_lines="3 6"
        from browserist import Browser, BrowserSettings, common_devices

        huawei_p40_lite = common_devices.Huawei.P40_LITE
            settings = BrowserSettings(
            headless=True,
            viewport=huawei_p40_lite)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    MATE_30_PRO = DeviceViewportSize(392, 800)
    MATE_30 = DeviceViewportSize(360, 780)

    MATE_20_LITE = DeviceViewportSize(360, 780)
    MATE_20_PRO = DeviceViewportSize(360, 780)

    MATE_10_LITE = DeviceViewportSize(360, 720)

    NOVA_7_PRO = DeviceViewportSize(360, 780)
    NOVA_7_SE = DeviceViewportSize(360, 800)
    NOVA_7_I = DeviceViewportSize(360, 770)

    NOVA_6 = DeviceViewportSize(360, 880)

    P40_PRO = DeviceViewportSize(400, 880)
    P40_LITE = DeviceViewportSize(360, 770)
    P40 = DeviceViewportSize(360, 780)

    P30_PRO = DeviceViewportSize(360, 780)
    P30_LITE = DeviceViewportSize(360, 771)
    P30 = DeviceViewportSize(360, 780)

    P20_PRO = DeviceViewportSize(360, 747)
    P20_LITE = DeviceViewportSize(360, 760)
    P20 = DeviceViewportSize(360, 748)

    P10_PLUS = DeviceViewportSize(360, 640)
    P10_LITE = DeviceViewportSize(360, 640)
    P10 = DeviceViewportSize(360, 640)

    P9_LITE = DeviceViewportSize(360, 640)
    P9 = DeviceViewportSize(360, 640)

    P8_LITE = DeviceViewportSize(360, 640)

    Y9_PRIME = DeviceViewportSize(360, 780)
    Y9_S = DeviceViewportSize(360, 780)
