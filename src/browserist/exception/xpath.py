class XPathSyntaxError(Exception):
    __slots__ = ["message"]

    def __init__(self, xpath: str) -> None:
        self.message = f"Invalid XPath syntax: {xpath}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
