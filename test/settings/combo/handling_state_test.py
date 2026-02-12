import pytest

from browserist.model.combo_settings.handling_state import ComboHandlingState, IsComboHandled


@pytest.mark.parametrize(
    "state, expectation",
    [
        (IsComboHandled.NOT_STARTED, None),
        (IsComboHandled.NOT_YET_BUT_SOON, False),
        (IsComboHandled.YES_AND_WITH_SUCCESS, True),
    ],
)
def test_set_and_get_combo_handled_state(state: IsComboHandled, expectation: bool | None) -> None:
    handling_state: ComboHandlingState = ComboHandlingState()
    handling_state.set(state)
    assert handling_state.get() is state
    assert handling_state.get_value() is expectation
