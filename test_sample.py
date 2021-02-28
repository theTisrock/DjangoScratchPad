
def increment(number):
    return number + 1


def test_passes():
    assert increment(5) == 6


def test_fails():
    assert increment(5) == 0
