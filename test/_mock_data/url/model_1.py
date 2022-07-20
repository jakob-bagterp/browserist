from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class URLExpectation:
    url: str
    expectation: Any


@dataclass(frozen=True, slots=True)
class URLTestSet:
    tests: list[URLExpectation]
