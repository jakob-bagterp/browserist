import subprocess

from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.type import BrowserType


def set_image_loading(browser_driver: BrowserDriver, load_images: bool = True) -> None:
    if browser_driver.settings.type is BrowserType.SAFARI:
        value = "true" if load_images else "false"
        subprocess.call(
            f"defaults write com.apple.Safari com.apple.Safari.ContentPageGroupIdentifier.WebKit2LoadsImagesAutomatically {value}".split())
        subprocess.call(
            f"defaults write com.apple.Safari com.apple.Safari.ContentPageGroupIdentifier.WebKit2LoadsImagesAutomatically {value}".split())


def disable_images(browser_driver: BrowserDriver) -> None:
    set_image_loading(browser_driver, load_images=False)


def enable_images(browser_driver: BrowserDriver) -> None:
    set_image_loading(browser_driver, load_images=True)
