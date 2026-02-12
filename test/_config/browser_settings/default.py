from browserist import BrowserSettings

DEFAULT = BrowserSettings(check_connection=False)

HEADLESS = BrowserSettings(headless=True, check_connection=False)

DISABLE_IMAGES = BrowserSettings(disable_images=True, check_connection=False)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(headless=True, disable_images=True, check_connection=False)

HEADLESS_AND_FIXED_SIZE = BrowserSettings(headless=True, check_connection=False, viewport=(1024, 768))
