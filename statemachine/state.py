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

        if will_enter is not None:
            self.will_enter = will_enter
        if entered is not None:
            self.entered = entered
        if will_exit is not None:
            self.will_exit = will_exit
        if exited is not None:
            self.exited = exited

    def will_enter(self):
        pass

    def entered(self):
        pass

    def will_exit(self):
        pass

    def exited(self):
        pass

    def __str__(self):
        return self.name
