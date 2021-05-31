import pytest
import leap_year

def test_four():
    for i in [2000, 2020, 2024]:
        assert leap_year.leap_year(i) == "yes"
    