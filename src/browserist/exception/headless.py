from ..model.browser.base.type import BrowserType

class HeadlessNotSupportedException(Exception):
    def __init__(self, browser_type: BrowserType) -> None:
        self.message = f"{browser_type.value}: This browser doesn't support headless."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
