from typing import Dict, Union, Optional, Callable

from statemachine.state import State
from statemachine.transition import Transition

class StateMachine:
    def __init__(self) -> None:
        self.states: Dict[str, State] = {}
        self.current_state: Optional[State] = None
        self.transitions: Dict[str, Transition] = {}
        self.add_overloads: Dict[str, Callable[[Union(State, Transition)], None]] = {
            'State': self._add_state,
            'Transition': self._add_transition
        }

    def add(self, new: Union[State, Transition]) -> None:
        self.add_overloads[type(new).__name__](new)

    def _add_state(self, new_state: State) -> None:
        self.states[new_state.name] = new_state
        if new_state.is_starting_state:
            self.current_state = new_state

    def _add_transition(self, t: Transition) -> None:
        is_declared: Callable[[str], bool] = lambda k: k in self.states
        assert is_declared(t.from_state_name), "Cannot transition from an undeclared state"
        assert all(t for t in map(is_declared, t.to_states_names)), "Canot transition to an undeclared state"
        self.transitions[t.from_state_name] = t

    def can_transition_to(self, state_name: str) -> bool:
        assert (state_name in self.states.keys()), "No such state " + state_name

        if self.current_state is not None:
            return state_name in self.transitions[self.current_state.name]
        raise Exception

    def transition_to(self, state_name: str) -> None:
        if self.can_transition_to(state_name):
            transition = self.transitions[self.current_state.name]
            old_state = self.current_state
            new_state = self.states[state_name]

            transition.before()
            self.current_state.will_exit()
            new_state.will_enter()

            self.current_state = new_state

            old_state.exited()
            self.current_state.entered()
            transition.after()
        else:
            raise Exception
