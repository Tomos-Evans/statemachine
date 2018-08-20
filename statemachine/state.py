from typing import Optional, Callable

class State:
    def __init__(self,
                 name: str,
                 is_starting_state: bool=False,
                 will_enter: Optional[Callable]=None,
                 entered: Optional[Callable]=None,
                 will_exit: Optional[Callable]=None,
                 exited: Optional[Callable]=None) -> None:

        self.is_starting_state = is_starting_state
        self.name = name

        self.will_enter = will_enter if will_enter else lambda : None
        self.entered = entered if entered else lambda : None
        self.will_exit = will_exit if will_exit else lambda : None
        self.exited = exited if exited else lambda : None

    def __str__(self):
        return self.name
