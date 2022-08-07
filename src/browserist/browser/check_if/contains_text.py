import re

from selenium.webdriver.common.by import By

from ...model.type.xpath import XPath


def check_if_contains_text(driver: object, xpath: str, regex: str, ignore_case: bool = True) -> bool:
    xpath = XPath(xpath)
    try:
        text = str(driver.find_element(By.XPATH, xpath).text)  # type: ignore
        if ignore_case:
            match = re.search(regex, text, re.IGNORECASE)
        else:
            match = re.search(regex, text)
        return bool(match)
    except Exception:
        return False
