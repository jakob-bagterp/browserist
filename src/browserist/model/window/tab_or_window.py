from enum import Enum, unique


@unique
class TabOrWindow(Enum):
    """Selector to open new tab or window.

    Attributes:
        TAB: Use for new tab.
        WINDOW: Use for new window.
    """

    TAB = "tab"
    WINDOW = "window"
