from enum import Enum, unique


@unique
class IsComboHandled(Enum):
    """Class to define handling states of combo method.

    Attributes:
        NOT_STARTED: Intended as inital value for handling variable.
        NOT_YET_BUT_SOON: Combo flow in progress and initial checks completed successfully.
        YES_AND_WITH_SUCCESS: Combo flow completed successfully.
    """

    NOT_STARTED = None  # Will be evaluated similar to False when used in conditional if statements.
    NOT_YET_BUT_SOON = False
    YES_AND_WITH_SUCCESS = True


class ComboHandlingState():
    """Class to define handling state of combo methods."""

    __slots__ = ["current", "current_value"]

    def __init__(self, state: IsComboHandled = IsComboHandled.NOT_STARTED) -> None:
        self.current: IsComboHandled
        self.current_value: bool | None
        self.set(state)

    def set(self, state: IsComboHandled) -> None:
        """Set current state"""

        self.current = state
        self.current_value = state.value

    def get(self) -> IsComboHandled:
        """Get current state"""

        return self.current

    def get_value(self) -> bool | None:
        """Get current state"""

        return self.current_value
