from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait
from ..wait.for_element import wait_for_element


def switch_to_iframe(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    iframe_element = get_element_without_wait(browser_driver, xpath)
    driver = browser_driver.get_webdriver()
    driver.switch_to.frame(iframe_element)
