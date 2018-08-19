from typing import Optional

class State:
    def __init__(self, name: str, is_starting_state: bool=False) -> None:
        self.is_starting_state = is_starting_state
        self.name = name

    def __str__(self):
        return self.name
