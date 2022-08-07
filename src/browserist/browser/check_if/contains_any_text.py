from selenium.webdriver.common.by import By

from ...model.type.xpath import XPath


def check_if_contains_any_text(driver: object, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        text = str(driver.find_element(By.XPATH, xpath).text)  # type: ignore
        return bool(text)
    except Exception:
        return False
