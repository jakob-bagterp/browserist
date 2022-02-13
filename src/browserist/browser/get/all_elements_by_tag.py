from typing import List
from ..wait.for_element import wait_for_element
from ...constant import timeout

def get_all_elements_by_tag(driver: object, tag: str, timeout: int = timeout.DEFAULT) -> List[object]:
    wait_for_element(driver, f"//{tag}", timeout)
    return driver.find_elements_by_tag_name(tag)
