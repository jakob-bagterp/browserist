from ..model.browser.base.driver import BrowserDriver


def disable_images(browser_driver: BrowserDriver) -> BrowserDriver:
    if browser_driver.settings.disable_images:
        preferences = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_settings.images": 2
        }
        browser_driver.chrome_options.add_experimental_option("prefs", preferences)
    return browser_driver


def enable_headless(browser_driver: BrowserDriver) -> BrowserDriver:
    if browser_driver.settings.headless:
        browser_driver.chrome_options.add_argument("--headless")  # type: ignore
    return browser_driver


def set_download_directory(browser_driver: BrowserDriver) -> BrowserDriver:
    if browser_driver.settings._download_dir is not None:
        preferences = {
            "download.default_directory": browser_driver.settings._download_dir,
            "download.directory_upgrade": True,
            "download.prompt_for_download": False
        }
        browser_driver.chrome_options.add_experimental_option("prefs", preferences)
    return browser_driver
