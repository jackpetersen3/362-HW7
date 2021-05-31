import pytest
import fizzBuzz

def test_three(capsys):
    for i in [3, 6, 9, 12]:
        fizzBuzz.fizzbuzz()
        out = capsys.readouterr().out.split('\n')[:-1]
        assert out[i]== 'Fizz'