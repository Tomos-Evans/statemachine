from typing import Dict, Union, Optional

from statemachine.state import State

class StateMachine:
    def __init__(self) -> None:
        self.states: Dict[str, State] = {}
        self.current_state: Optional[State] = None

    def add_state(self, new_state: State) -> None:
        self.states[new_state.name] = new_state
