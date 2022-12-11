from enum import Enum, unique


@unique
class ComboHandlingState(Enum):
    """Class to define handling states of combo method."""

    # Intended as inital value for handling variable:
    NOT_STARTED = None  # NB: Will be evaluated similar to False when used in conditional if statements.

    # Combo flow in progress and initial checks completed successfully:
    NOT_YET = False

    # Combo flow completed successfully:
    YES_AND_WITH_SUCCESS = True
