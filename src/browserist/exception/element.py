from ..browser.get.url.current import get_current_url


class NoElementFoundException(Exception):
    def __init__(self, driver: object, xpath: str) -> None:
        current_url = get_current_url(driver)
        self.message = f"On page {current_url}, no such element found while waiting: {xpath}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class NoElementFoundWithTextConditionException(Exception):
    def __init__(self, driver: object, xpath: str, text_condition: str) -> None:
        current_url = get_current_url(driver)
        self.message = f"On page {current_url}, an element that contains \"{text_condition}\" could not be found: {xpath}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class NoElementDimensionsFoundException(Exception):
    def __init__(self, driver: object, xpath: str) -> None:
        current_url = get_current_url(driver)
        self.message = f"On page {current_url}, no such element found while trying to get element dimensions: {xpath}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
