from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class W3SchoolsCom:
    SEARCH_INPUT = "//input[@id='search2']"
