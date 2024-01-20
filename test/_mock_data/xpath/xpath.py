from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class W3SchoolsCom:
    SEARCH_INPUT = "//input[@id='search2']"


@dataclass(slots=True, frozen=True)
class DropDownSeletor:
    DROPDOWN_OPTIONS = "//select[@id='options']"
    OPTION_1 = f"{DROPDOWN_OPTIONS}/option[@value='option1']"
    OPTION_2 = f"{DROPDOWN_OPTIONS}/option[@value='option2']"
    OPTION_3 = f"{DROPDOWN_OPTIONS}/option[@value='option3']"
    OPTION_4 = f"{DROPDOWN_OPTIONS}/option[@value='option4']"


@dataclass(slots=True, frozen=True)
class DownloadPage:
    DONWLOAD_BUTTON = "//button[@id='download']"
