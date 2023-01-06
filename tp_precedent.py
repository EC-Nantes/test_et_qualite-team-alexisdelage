import pytest

def func(x):
    return x + 1
def test_answer():
    assert func(3) == 4

def f():
    raise SystemExit(1)
def test_mytest():
    with pytest.raises(SystemExit):
        f()

class TestClass:
    @pytest.mark.skip(reason="ok ok")
    def test_one(self):
        x = "this"
        assert "h" in x
    
    @pytest.mark.xfail
    def test_two(self):
        x = "hello"
        # hasattr() method returns true if an object has the
        # given named attribute and false if it does not
        assert hasattr(x, "check")

class TestClassDemoInstance:
    value = 0
    #@pytest.mark.xfail
    def test_one(self):
        self.value = 1
        assert self.value == 1
    def test_two(self):
        assert self.value == 0

import time
def test_funcfast():
    time.sleep(0.1)
def test_funcslow1():
    time.sleep(0.2)
def test_funcslow2():
    time.sleep(0.3)

@pytest.fixture()
def dataset():
    """Return some data to test functions"""
    return {'data1': 1, 'data2': 2}
def test_dataset(dataset):
    """test and confirm fixture value"""
    assert dataset == {'data1': 1, 'data2': 2}

@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected
