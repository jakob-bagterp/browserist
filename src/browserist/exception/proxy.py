from ..model.browser.base.type import BrowserType


class ProxyNotSupportedException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_type: BrowserType) -> None:
        self.message = f"{browser_type.value}: This browser doesn't support using a proxy server."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
