class URLSyntaxError(Exception):
    __slots__ = ["message"]

    def __init__(self, url: str) -> None:
        self.message = f"Invalid URL syntax: {url}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
