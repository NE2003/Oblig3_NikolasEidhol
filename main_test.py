from Oblig3_NikolasEidhol.main import *


# A year is a leap year when the year is divisible by 4 but not 100 OR when it is divisible by 400
def test_if_divisible_by_four_but_not_one_hundred():
    assert isLeapYear(2004) == True
    assert isLeapYear(2024) == True
    assert isLeapYear(2044) == True


def test_if_divisible_by_four_hundred():
    assert isLeapYear(2000) == True
    assert isLeapYear(2400) == True
    assert isLeapYear(2800) == True


# A year is NOT a leap year when it is not divisible by 4 OR when it is divisible by 100, but not 400

def test_if_not_divisible_by_four():
    assert isLeapYear(2001) == False
    assert isLeapYear(2002) == False
    assert isLeapYear(2003) == False


def test_if_divisible_by_one_hundred_but_not_four_hundred():
    assert isLeapYear(2001) == False
    assert isLeapYear(2002) == False
    assert isLeapYear(2003) == False
