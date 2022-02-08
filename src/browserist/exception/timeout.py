from ..browser.get_current_url import get_current_url
from ..browser.get_current_page_title import get_current_page_title

class WaitForElementTimeoutException(Exception):
    def __init__(self, driver: object, xpath: str) -> None:
        current_url = get_current_url(driver)
        self.message = f"On page {current_url}, waiting for element timed out: {xpath}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

class WaitForPageTitleToChangeTimeoutException(Exception):
    def __init__(self, driver: object, page_title_or_fragment: str) -> None:
        current_url = get_current_url(driver)
        current_page_title = get_current_page_title(driver)
        self.message = f"On page {current_url} with title \"{current_page_title}\", check of page title fragment timed out, or the title fragment doesn't match: {page_title_or_fragment}"
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
