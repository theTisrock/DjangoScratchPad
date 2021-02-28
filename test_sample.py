

def increment(number):
    return number + 1


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def test_passes():
    assert increment(5) == 6


def test_fails():
    assert increment(5) == 0


class TestMath:

    def test_increment(self):
        assert increment(5) == 6  # pass

    def test_add(self):
        assert add(1, 1) == 10  # fail

    def test_subtract(self):
        assert subtract(10, 9) == 1
