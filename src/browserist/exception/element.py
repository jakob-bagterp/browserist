from ..browser.get.url.current import get_current_url
from ..model.browser.base.driver import BrowserDriver


class NoElementFoundException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_driver: BrowserDriver, xpath: str) -> None:
        current_url = get_current_url(browser_driver)
        self.message = f"On page {current_url}, no such element found while waiting: {xpath}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class NoElementFoundWithTextConditionException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_driver: BrowserDriver, xpath: str, text_condition: str) -> None:
        current_url = get_current_url(browser_driver)
        self.message = f'On page {current_url}, an element that contains "{text_condition}" could not be found: {xpath}'
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class NoElementDimensionsFoundException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_driver: BrowserDriver, xpath: str) -> None:
        current_url = get_current_url(browser_driver)
        self.message = f"On page {current_url}, no such element found while trying to get element dimensions: {xpath}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
