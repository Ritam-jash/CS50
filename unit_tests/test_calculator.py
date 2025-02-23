# Test the code using if statement
from unit_tests.calculator import squar

def main():
    test_squar()


def test_squar():
    if squar(2) != 4:
        print("2 squar is not 4")
    if squar(3) != 9:
        print("3 squar is not 9")

if __name__ == "__main__":
    main()


# Test the code assert keyword
from unit_tests.calculator import squar

def main():
    test_squar()


def test_squar():
    assert squar(2) == 4
    assert squar(3) == 9

if __name__ == "__main__":
    main()


# TAW now we handel the assertionError us try and except
from unit_tests.calculator import squar

def main():
    test_squar()


def test_squar():
    try:
        assert squar(2) == 4
    except AssertionError:
        print("2 squar is not 4")
    try:
        assert squar(3) == 9
    except AssertionError:
        print("3 squar is not 9")
    try:
        assert squar(-2) == 4
    except AssertionError:
        print("-2 squar is not 4")
    try:
        assert squar(-3) == 9
    except AssertionError:
        print("-3 squar is not 9")
    try:
        assert squar(0) == 0
    except AssertionError:
        print("o squar is not 0")


if __name__ == "__main__":
    main()


# NOW WE LEARN TO BEST WAY TO TEST THE CODE USING pytest
from unit_tests.calculator import squar


def test_squar():
    assert squar(2) == 4
    assert squar(3) == 9
    assert squar(-2) == 4
    assert squar(-3) == 9
    assert squar(0) == 0


# Now we test the code via seperate [RIGHT WAY TO TEST THE CODE]
from unit_tests.calculator import squar

def test_positive():
    assert squar(2) == 4
    assert squar(3) == 9

def test_negative():
    assert squar(-2) == 4
    assert squar(-3) == 9

def test_zero():
    assert squar(0) == 0


# Now we test the string using raises function
import pytest
from unit_tests.calculator import squar

def test_positive():
    assert squar(2) == 4
    assert squar(3) == 9

def test_negative():
    assert squar(-2) == 4
    assert squar(-3) == 9

def test_zero():
    assert squar(0) == 0 

def test_str():
    with pytest.raises(TypeError):
        squar("cat")