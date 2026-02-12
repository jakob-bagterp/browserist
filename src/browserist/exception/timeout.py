from ..browser.get.page_title import get_page_title
from ..browser.get.url.current import get_current_url
from ..model.browser.base.driver import BrowserDriver


class WaitForElementTimeoutException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_driver: BrowserDriver, xpath: str) -> None:
        current_url = get_current_url(browser_driver)
        self.message = f"On page {current_url}, waiting for element timed out: {xpath}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class WaitForPageTitleToChangeTimeoutException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_driver: BrowserDriver, page_title_or_fragment: str) -> None:
        current_url = get_current_url(browser_driver)
        page_title = get_page_title(browser_driver)
        self.message = f'On page {current_url} with title "{page_title}", check of page title fragment timed out, or the title fragment doesn\'t match: {page_title_or_fragment}'
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class WaitForUrlTimeoutException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_driver: BrowserDriver, url: str) -> None:
        current_url = get_current_url(browser_driver)
        self.message = f"On page {current_url}, waiting for URL timed out, or the URL fragment doesn't exist: {url}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class WaitForWindowTimeoutException(Exception):
    __slots__ = ["message"]

    def __init__(self) -> None:
        self.message = "Waiting for new tab or window to open timed out."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
