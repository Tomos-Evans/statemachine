from typing import Dict, List, Optional, Callable

class Transition(Dict[str, List[str]]):
    def __init__(self,
                 k:Optional[str]=None,
                 v: Optional[List[str]]=None,
                 before: Optional[Callable]=None,
                 after: Optional[Callable]=None) -> None:

        super(Transition, self).__init__()

        if (k is not None) and (v is not None):
            self[k] = v

        if before is not None:
            self.before = before

        if after is not None:
            self.after = after

    def before(f: Callable) -> None:
        pass

    def after(f: Callable) -> None:
        pass

    def __str__(self):
        return "\n".join([k + " -> " + str(self[k]) for k in self.keys()])

    def __contains__(self, state_name: str) -> bool:
        return state_name in self[list(self.keys())[0]]
