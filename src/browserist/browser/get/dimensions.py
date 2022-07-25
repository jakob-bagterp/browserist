from selenium.webdriver.common.by import By

from ...model.browser.base.settings import BrowserSettings
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_dimensions(driver: object, settings: BrowserSettings, xpath: str, timeout: int) -> tuple[int, int]:
    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    # Returns dictionary object, e.g. {'height': 598, 'width': 479}:
    dimensions: dict[str, int] = driver.find_element(By.XPATH, xpath).size  # type: ignore
    return dimensions.get("width") or 0, dimensions.get("height") or 0
