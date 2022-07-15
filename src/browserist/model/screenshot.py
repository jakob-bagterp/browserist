from enum import Enum, unique


@unique
class ScreenshotType(Enum):
    """Class to define screenshot type, e.g. complete page, visible portion, element."""

    COMPLETE_PAGE = "complete page"
    ELEMENT = "element"
    VISIBLE_PORTION = "visible portion"
