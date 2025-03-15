from ..model.browser.base.type import BrowserType


class HeadlessModeNotSupportedException(Exception):
    __slots__ = ["message"]

    def __init__(self, browser_type: BrowserType) -> None:
        self.message = f"{browser_type.value}: This browser doesn't support headless mode."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class MethodNotSupportedInHeadlessModeException(Exception):
    __slots__ = ["message"]

    def __init__(self, method_name: str, reason: str) -> None:
        self.message = f"Method \"{method_name}\" not supported in headless mode since {reason}."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
