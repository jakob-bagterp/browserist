from ...exception.user_agent import ChangeUserAgentOnTheFlyNotSupportedException
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.type import BrowserType


def set_user_agent(browser_driver: BrowserDriver, user_agent: str) -> None:
    match browser_driver.settings.type:
        case BrowserType.CHROME | BrowserType.EDGE:
            driver = browser_driver.get_webdriver()
            driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})
        case _:
            raise ChangeUserAgentOnTheFlyNotSupportedException(browser_driver.settings.type)
    driver = browser_driver.get_webdriver()
