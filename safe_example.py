from statemachine import StateMachine, State, Transition


class Safe(StateMachine):
    def __init__(self, pin_code):
        super().__init__()

        self.pin_code = pin_code

        self.add(State('locked', is_starting_state=True))
        self.add(State('unlocked'))
        self.add(State('broken'))

        self.add(Transition('locked', ['unlocked', 'broken']))
        self.add(Transition('unlocked', ['locked', 'broken']))

    def try_combination(self, combination):
        if self.pin_code == combination and self.can_transition_to('unlocked'):
            self.transition_to('unlocked')

    def lock(self):
        if self.can_transition_to('locked'):
            self.transition_to('locked')

    def force_lock(self):
        if self.can_transition_to('broken'):
            self.transition_to('broken')


safe = Safe(pin_code=1234)
print(safe.current_state) # locked

safe.try_combination(123)
print(safe.current_state) # locked

safe.try_combination(1234)
print(safe.current_state) # unlocked

safe.lock()
print(safe.current_state) # locked

safe.force_lock()
print(safe.current_state) # broken
