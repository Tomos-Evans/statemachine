from typing import List, Optional, Callable

class Transition():
    def __init__(self,
                 from_state_name:str,
                 to_states_names: List[str],
                 before: Optional[Callable]=None,
                 after: Optional[Callable]=None) -> None:

        self.from_state_name = from_state_name
        self.to_states_names = to_states_names

        self.before = before if before else lambda : None
        self.after = after if after else lambda : None

    def __str__(self):
        return self.from_state_name + " -> " + ", ".join(self.to_states_names)

    def __contains__(self, state_name: str) -> bool:
        return state_name in self.to_states_names
