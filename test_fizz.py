import pytest
import fizzBuzz

def test_three(capsys):
    for i in [2, 5, 8, 11]:
        fizzBuzz.fizzbuzz()
        out = capsys.readouterr().out.split('\n')[:-1]
        assert out[i]== 'Fizz'
def test_five(capsys):
    for i in [4, 9, 19, 24]:
        fizzBuzz.fizzbuzz()
        out = capsys.readouterr().out.split('\n')[:-1]
        assert out[i]== 'Buzz'
def test_3_5(capsys):
    for i in [14, 29]:
        fizzBuzz.fizzbuzz()
        out = capsys.readouterr().out.split('\n')[:-1]
        assert out[i]== 'FizzBuzz'
