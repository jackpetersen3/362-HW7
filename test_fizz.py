import pytest
import fizzBuzz

def test_three:
    for i in [3, 6, 9, 12]:
        assert fizzbuzz.fizzbuzz(i) == "Fizz"