from __future__ import annotations

from ... import helper
from ...exception.ip import IPv4SyntaxError


class IPv4(str):
    """Class to handle and validate IPv4 input as "tiny type"."""

    __slots__ = ["value"]

    def __new__(cls, ip: str) -> IPv4:
        # If input already is a validated IPv4 element, bypass and don't create a new object:
        return ip if isinstance(ip, IPv4) else super().__new__(cls, ip)

    def __init__(self, ip: str) -> None:
        if not helper.ip.ipv4_is_valid(ip):
            raise IPv4SyntaxError(ip)
        self.value: str = ip

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value

    def is_valid(self) -> bool:
        return helper.ip.ipv4_is_valid(self.value)
