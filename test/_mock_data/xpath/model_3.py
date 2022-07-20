from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class XPathExpectation:
    xpath: str
    expectation: Any


@dataclass(frozen=True, slots=True)
class XPathTestSet:
    url: str
    tests: list[XPathExpectation]
