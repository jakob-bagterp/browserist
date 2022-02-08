from ..browser.get import get_current_url

class WaitTimeoutException(Exception):
    def __init__(self, driver: object, xpath: str) -> None:
        current_url = get_current_url(driver)
        self.message = f"On page {current_url}, waiting for element timed out: {xpath}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

class WaitForUrlTimeoutException(Exception):
    def __init__(self, driver: object, url: str) -> None:
        current_url = get_current_url(driver)
        self.message = f"On page {current_url}, waiting for URL timed out, or the URL fragment doesn't exist: {url}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
