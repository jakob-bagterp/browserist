from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class w3schools_com:
    SEARCH_INPUT = "//input[@id='search2']"
