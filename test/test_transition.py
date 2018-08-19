from statemachine import Transition

class TestContains():
    def test_value_is_contained(self):
        assert 'a1' in Transition('a', ['a1','b1','c1'])
        assert 'b1' in Transition('a', ['a1','b1','c1'])
        assert 'c1' in Transition('a', ['a1','b1','c1'])

    def test_from_state_check(self):
        assert 'from' not in Transition('from', ['to'])

    def test_value_not_contained(self):
        assert 'not_there' not in Transition('a', ['b'])

class TestHooks():
    def test_empty_hooks(self):
        t = Transition('a', ['b'])
        assert t.before() == None
        assert t.after() == None

    def sample_hook(self, n):
        def h():
            return n
        return h

    def test_before(self):
        t = Transition('a', ['b'], before=self.sample_hook(4))
        assert t.before() == 4
        assert t.after() == None

    def test_after(self):
        t = Transition('a', ['b'], after=self.sample_hook(4))
        assert t.after() == 4
        assert t.before() == None

    def test_both_hooks(self):
        t = Transition('a', ['b'], before=self.sample_hook(4), after=self.sample_hook(5))
        assert t.before() == 4
        assert t.after() == 5

class TestConstruction():
    def test_standard_construction(self):
        t = Transition('a', ['b', 'c'])
        assert t.from_state_name == 'a'
        assert t.to_states_names == ['b', 'c']

class Test_String():
    def test_string_representation(self):
        t = Transition('a', ['b', 'c'])
        assert str(t) == "a -> b, c"
