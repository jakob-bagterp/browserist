from browserist import BrowserSettings

DEFAULT = BrowserSettings()

HEADLESS = BrowserSettings(
    headless=True
)

DISABLE_IMAGES = BrowserSettings(
    disable_images=True
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    headless=True,
    disable_images=True
)
