from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.type import BrowserType


def disable_images(browser_driver: BrowserDriver) -> BrowserDriver:
    if browser_driver.settings.disable_images:
        preferences = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_settings.images": 2,
        }
        match browser_driver.settings.type:
            case BrowserType.CHROME:
                browser_driver.chrome_options.add_experimental_option("prefs", preferences)
            case BrowserType.EDGE:
                browser_driver.edge_options.use_chromium = True  # type: ignore
                browser_driver.edge_options.add_experimental_option("prefs", preferences)
            case _:
                pass
    return browser_driver


def set_download_directory(browser_driver: BrowserDriver) -> BrowserDriver:
    if browser_driver.settings._download_dir is not None:
        preferences = {
            "download.default_directory": browser_driver.settings._download_dir,
            "download.directory_upgrade": True,
            "download.prompt_for_download": False,
        }
        match browser_driver.settings.type:
            case BrowserType.CHROME:
                browser_driver.chrome_options.add_experimental_option("prefs", preferences)
            case BrowserType.EDGE:
                browser_driver.edge_options.add_experimental_option("prefs", preferences)
            case _:
                pass
    return browser_driver
