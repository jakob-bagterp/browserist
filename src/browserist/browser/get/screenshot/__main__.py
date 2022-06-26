from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .complete_page import get_screenshot_complete_page
from .visible_portion import get_screenshot_visible_portion


class GetScreenshotDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def complete_page(self, file_name: str | None = None, destination_dir: str | None = None) -> None:
        """Take screenshot of complete page and save as PNG image. Default destination directory is from where the script is executed. Examples:

        browser.get.screenshot.complete_page() # Default file name and destination

        browser.get.screenshot.complete_page("image.png") # Custom file name and default destination

        browser.get.screenshot.complete_page("image.png", "./screenshots") # Custom file name and destination

        browser.get.screenshot.complete_page(destination_dir = "./screenshots") # Default file name and custom destination"""

        get_screenshot_complete_page(self._driver, self._settings, file_name, destination_dir)

    def visible_portion(self, file_name: str | None = None, destination_dir: str | None = None) -> None:
        """Take screenshot and save as PNG image. Default destination directory is from where the script is executed. Examples:

        browser.get.screenshot.visible_portion() # Default file name and destination

        browser.get.screenshot.visible_portion("image.png") # Custom file name and default destination

        browser.get.screenshot.visible_portion("image.png", "./screenshots") # Custom file name and destination

        browser.get.screenshot.visible_portion(destination_dir = "./screenshots") # Default file name and custom destination"""

        get_screenshot_visible_portion(self._driver, self._settings, file_name, destination_dir)
