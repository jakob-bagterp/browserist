from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class FilePNGExpectation:
    file_name: str
    expactation: Any


@dataclass(frozen=True, slots=True)
class FilePNGTestSet:
    tests: list[FilePNGExpectation]
