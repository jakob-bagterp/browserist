from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.safari.options import Options as SafariOptions

from ..model.browser.base.driver import BrowserDriver


def page_load_strategy(browser_driver: BrowserDriver, options: ChromeOptions | EdgeOptions | FirefoxOptions | IEOptions | SafariOptions) -> ChromeOptions | EdgeOptions | FirefoxOptions | IEOptions | SafariOptions:
    options.page_load_strategy = browser_driver.settings.page_load_strategy.value
    return options
