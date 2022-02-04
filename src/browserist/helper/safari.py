import subprocess
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.type import BrowserType

def disable_images(browser_driver: BrowserDriver) -> None:
    if browser_driver.settings.type is BrowserType.SAFARI:
        subprocess.call("defaults write com.apple.Safari com.apple.Safari.ContentPageGroupIdentifier.WebKit2LoadsImagesAutomatically false".split())
        subprocess.call("defaults write com.apple.Safari com.apple.Safari.ContentPageGroupIdentifier.WebKit2LoadsImagesAutomatically false".split())
