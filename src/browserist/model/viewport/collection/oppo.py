from dataclasses import dataclass

from ..device import DeviceViewportSize


@dataclass(slots=True, frozen=True)
class OppoDevices:
    """Viewport sizes for common Oppo devices.

    Example:
        ```python title="" linenums="1" hl_lines="3 6"
        from browserist import Browser, BrowserSettings, common_devices

        oppo_f1_plus = common_devices.Oppo.F1_PLUS
            settings = BrowserSettings(
            headless=True,
            viewport=oppo_f1_plus)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    F1_PLUS = DeviceViewportSize(360, 740)  # TODO: To be verified.
    F1 = DeviceViewportSize(360, 740)  # TODO: To be verified.

    R9_PLUS = DeviceViewportSize(360, 740)  # TODO: To be verified.
    R9 = DeviceViewportSize(360, 740)  # TODO: To be verified.

    A53 = DeviceViewportSize(360, 740)  # TODO: To be verified.
    A37 = DeviceViewportSize(360, 640)
