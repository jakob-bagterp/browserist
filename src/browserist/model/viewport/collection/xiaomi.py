from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class XiaomiDevices:
    """Viewport sizes for common Xiaomi devices.

    Example:
        ```python title="" linenums="1" hl_lines="3 6"
        from browserist import Browser, BrowserSettings, common_devices

        xiaomi_mi_10_pro = common_devices.Xiaomi.MI_10_PRO
            settings = BrowserSettings(
            headless=True,
            viewport=xiaomi_mi_10_pro)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    MI_10T_PRO = DeviceViewportSize(393, 873)
    MI_10T = DeviceViewportSize(393, 873)
    MI_10_PRO = DeviceViewportSize(393, 851)
    MI_10 = DeviceViewportSize(393, 851)

    MI_9T = DeviceViewportSize(393, 851)
    MI_9_LITE = DeviceViewportSize(393, 851)
    MI_9_SE = DeviceViewportSize(393, 851)
    MI_9 = DeviceViewportSize(393, 851)

    MI_8_PRO = DeviceViewportSize(393, 817)
    MI_8_SE = DeviceViewportSize(393, 816)
    MI_8 = DeviceViewportSize(393, 817)

    MI_6 = DeviceViewportSize(393, 816)

    MI_3 = DeviceViewportSize(360, 640)

    REDMI_NOTE_9_PRO = DeviceViewportSize(393, 873)
    REDMI_NOTE_9 = DeviceViewportSize(393, 851)

    REDMI_NOTE_8_PRO = DeviceViewportSize(393, 851)
    REDMI_NOTE_8 = DeviceViewportSize(393, 851)

    REDMI_NOTE_7 = DeviceViewportSize(393, 851)
