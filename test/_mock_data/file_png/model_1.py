from dataclasses import dataclass
from typing import Any

from _mock_data.url import internal_url
from _mock_data.xpath.test_set_3 import VALID_XPATH


@dataclass(frozen=True, slots=True)
class FilePNGExpectation:
    file_name: str
    expectation: Any
    url: str = internal_url.EXAMPLE_COM
    xpath: str = VALID_XPATH


@dataclass(frozen=True, slots=True)
class FilePNGTestSet:
    tests: list[FilePNGExpectation]
