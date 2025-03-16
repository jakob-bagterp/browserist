class IPv4SyntaxError(Exception):
    __slots__ = ["message"]

    def __init__(self, ip: str) -> None:
        self.message = f"Invalid IPv4 syntax: {ip}. Should be an IP address ranging from `0.0.0.0` to `255.255.255.255`."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
