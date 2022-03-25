from .is_element_enabled import check_if_is_element_enabled


def check_if_is_element_disabled(driver: object, xpath: str) -> bool:
    return not check_if_is_element_enabled(driver, xpath)
