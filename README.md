# state-machine
A simple state machine library for Python.

## Example
A simple safe has three states:
1. `unlocked` and can be opened
2. `locked` so that is does not open easily, but you can try to force it
3. `broken` the lock was forced and is now broken, can never recover from this

Here is a simple implementation to illistrate the state machine lib.

``` Python
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
```

### Hooks
The statemachine library also provides *hooks* that can be triggered by state events or whole transitions.

#### State Hooks

``` Python
will_enter_offline = lambda : print("About to enter the offline state")
self.add(State('offline', will_enter=will_enter_offline))
```

The state hooks that are provided are:
1. `will_enter` - called before the machine enters the state
2. `entered` - called immediately after the state is entered
3. `will_exit` - called when the state is about to be exited
4. `exited` - called immediately after the state is exited

#### Transition Hooks
Transition hooks are more high level than state hooks, and as the name suggests they apply to an entire transition rather than a specific state.

``` Python
before = lambda : print("Before the transition takes place")
self.add(Transition('online', ['offline'], before=before)
```

The transition hooks provided are:
1. `before` - called before the transition happens
2. `after` - called after the transition happens


#### Hook execution order
The order in which state and transition hooks are executed is as follows:
1. before (transition)
2. will_exit (of the current state)
3. will_enter (of the new state)
4. **State change**
5. exited (of the preivious state)
6. entered (of the new current state)
7. after (of the transition)
