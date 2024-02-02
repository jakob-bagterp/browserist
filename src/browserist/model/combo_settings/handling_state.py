from enum import Enum, unique


@unique
class IsComboHandled(Enum):
    """Class to define handling states of combo method."""

    # Intended as inital value for handling variable:
    NOT_STARTED = None  # NB: Will be evaluated similar to False when used in conditional if statements.

    # Combo flow in progress and initial checks completed successfully:
    NOT_YET_BUT_SOON = False

    # Combo flow completed successfully:
    YES_AND_WITH_SUCCESS = True


class ComboHandlingState():
    """Class to define handling state of combo methods."""

    __slots__ = ["current"]

    def __init__(self, state: IsComboHandled = IsComboHandled.NOT_STARTED) -> None:
        self.set(state)

    def set(self, state: IsComboHandled) -> None:
        """Set current state"""

        self.current = state.value

    def get(self) -> bool | None:
        """Get current state"""

        return self.current