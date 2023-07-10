from .... import helper
from ....model.browser.base.driver import BrowserDriver
from .current import get_current_url


def get_current_domain(browser_driver: BrowserDriver) -> str:
    url = get_current_url(browser_driver)
    return helper.url.get_domain_from_url(url)
