class IPv4SyntaxError(Exception):
    __slots__ = ["message"]

    def __init__(self, ip: str) -> None:
        self.message = f"Invalid IPv4 syntax: {ip}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
