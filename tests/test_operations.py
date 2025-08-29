from calculator.operations import add
from calculator.operations import subtract


def test_add():
    assert add(4, 5) == 9


def test_subtract():
    assert subtract(4, 5) == -1


if __name__ == '__main__':
    test_add()
    test_subtract()
