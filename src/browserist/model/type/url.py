from __future__ import annotations

from ... import helper
from ...exception.url import URLSyntaxError


class URL(str):
    """Class to handle and validate URL input as "tiny type"."""

    __slots__ = ["value"]

    def __new__(cls, url: str | URL) -> URL:
        # If input already is a validated URL element, bypass and don't create a new object:
        return url if isinstance(url, URL) else super().__new__(cls, url)

    def __init__(self, url: str) -> None:
        if not helper.url.is_valid(url):
            raise URLSyntaxError(url)
        self.value: str = url

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value

    def is_valid(self) -> bool:
        return helper.url.is_valid(self.value)
