class XPath(str):
    def __new__(cls, xpath: str):
        return super().__new__(cls, xpath)
