import pytest
import leap_year

def test_four():
    for i in [2000, 2020, 2024]:
        assert leap_year.leap_year(i) == "yes"
def test_100_and_400():
    for i in [1600, 2000, 2400]:
        assert leap_year.leap_year(i) == "yes"
def test_100_only():
    for i in [1700, 2100, 2300]:
        assert leap_year.leap_year(i) == "no"
    