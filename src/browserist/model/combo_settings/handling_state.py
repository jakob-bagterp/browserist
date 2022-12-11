from enum import Enum, unique


@unique
class ComboHandlingState(Enum):
    """Class to define handling states of combo method."""

    # Intended as inital value for handling variable. Will be evaluated to False for conditional if statements:
    NOT_STARTED = None

    # Combo flow in progress and initial checks completed successfully:
    NOT_YET = False

    # Combo flow completed successfully:
    YES_AND_WITH_SUCCESS = True
