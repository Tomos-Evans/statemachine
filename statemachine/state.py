class State:
    def __init__(self, name: str) -> None:
        if not name:
            raise StateNameError()
        self.name = name

class StateNameError(Exception):
    pass
