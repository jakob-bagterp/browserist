from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class DownloadPage:
    DONWLOAD_BUTTON = "//button[@id='download']"
