import pytest

from statemachine import StateMachine, State, Transition

def test_creation():
    sm = StateMachine()
    assert sm.states == {}
    assert sm.current_state == None
    assert sm.transitions == {}

class TestAdd():
    def test_add_state(self):
        sm = StateMachine()

        s = State('s')
        sm.add(s)
        assert sm.states == {'s': s}

    def test_add_Transition(self):
        sm = StateMachine()
        sm.add(State('f'))
        sm.add(State('t'))

        t = Transition('f', ['t'])
        sm.add(t)
        assert sm.transitions == {'f': t}

    def test_new_transition_needs_existing_from_state(self):
        sm = StateMachine()
        sm.add(State('t'))

        with pytest.raises(AssertionError):
            t = Transition('f', ['t'])
            sm.add(t)

    def test_new_transition_needs_existing_to_state(self):
        sm = StateMachine()
        sm.add(State('t'))

        with pytest.raises(AssertionError):
            t = Transition('f', ['t'])
            sm.add(t)

    def test_adding_invalid_type(self):
        sm = StateMachine()

        with pytest.raises(Exception):
            sm.add('j')

class TestCanTransitonTo():
    def test_can_transition(self):
        sm = StateMachine()
        sm.add(State('online', is_starting_state=True))
        sm.add(State('offline'))
        sm.add(State('error'))

        sm.add(Transition('online', ['offline', 'error']))

        assert sm.can_transition_to('offline')
        assert sm.can_transition_to('error')

    def test_cant_transition_without_starting_state(self):
        sm = StateMachine()
        sm.add(State('online'))
        sm.add(State('offline'))
        sm.add(State('error'))

        sm.add(Transition('online', ['offline', 'error']))

        with pytest.raises(Exception):
            sm.can_transition_to('offline')
            sm.can_transition_to('error')

    def test_transitions_arent_two_way(self):
        sm = StateMachine()
        sm.add(State('online', is_starting_state=True))
        sm.add(State('offline'))

        sm.add(Transition('offline', ['online']))

        assert not sm.can_transition_to('offline')

    def test_cant_transition_to_undefined_state(self):
        sm = StateMachine()

        with pytest.raises(Exception):
            sm.can_transition_to('offline')

class TestTransition():
    def test_cant_transition_where_cant_transition_to(self):
        sm = StateMachine()
        sm.add(State('online', is_starting_state=True))
        sm.add(State('offline'))

        sm.add(Transition('offline', ['online']))

        assert not sm.can_transition_to('offline')
        with pytest.raises(Exception):
            sm.transition_to('offline')

    def test_hooks_order(self):
        result = []
        def hook(s):
            def h():
                result.append(s)
            return h

        sm = StateMachine()
        sm.add(State('online', is_starting_state=True, will_exit=hook('onwex'), exited=hook('onex')))
        sm.add(State('offline', will_enter=hook('ofwen'), entered=hook('ofen')))

        sm.add(Transition('online', ['offline'], before=hook('tb'), after=hook('ta')))
        sm.transition_to('offline')

        assert result == ['tb', 'onwex', 'ofwen', 'onex', 'ofen', 'ta']

    def test_transition(self):
        sm = StateMachine()
        sm.add(State('online', is_starting_state=True))
        sm.add(State('offline'))

        sm.add(Transition('online', ['offline']))
        sm.transition_to('offline')
