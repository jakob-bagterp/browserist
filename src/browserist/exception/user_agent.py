from ..model.browser.base.type import BrowserType


class CustomUserAgentNotSupportedException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_type: BrowserType) -> None:
        self.message = f"{browser_type.value}: This browser doesn't support setting a custom user agent."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class ChangeUserAgentOnTheFlyNotSupportedException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_type: BrowserType) -> None:
        self.message = f"{browser_type.value}: This browser doesn't support setting a custom user agent on the fly."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
