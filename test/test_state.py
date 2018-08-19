from statemachine import State

def test_string():
    s = State('s')
    assert str(s) == 's'

class TestHooks:
    def test_empty(self):
        s = State('s')
        assert s.will_enter() == None
        assert s.will_exit() == None
        assert s.entered() == None
        assert s.exited() == None

    def sample_hook(self, n):
        def h():
            return n
        return h

    def test_hooks(self):
        s = State('s',
                will_enter=self.sample_hook('wen'),
                will_exit=self.sample_hook('wex'),
                entered=self.sample_hook('en'),
                exited=self.sample_hook('ex'))

        assert s.will_enter() == 'wen'
        assert s.will_exit() == 'wex'
        assert s.entered() == 'en'
        assert s.exited() == 'ex'

class TestStartingState():
    def test_is_not(self):
        s = State('s')
        assert not s.is_starting_state

    def test_is(self):
        s = State('s', is_starting_state=True)
        assert s.is_starting_state
