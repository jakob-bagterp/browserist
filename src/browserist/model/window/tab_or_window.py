from enum import Enum, unique


@unique
class TabOrWindow(Enum):
    """Selector to open new tab or window.

    TAB: Use for new tab.

    CONTINUE: Use for new window."""

    TAB = "tab"
    WINDOW = "window"
