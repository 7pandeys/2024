import pytest
from src.prime_numbers import prime_numbers

def test_prime_number():
    assert prime_numbers(11) == "11 is Prime Number"

def test_non_prime_number():
    assert prime_numbers(10) == "10 is Not Prime Number"

def test_smallest_prime():
    assert prime_numbers(2) == "2 is Prime Number"

def test_one():
    assert prime_numbers(1) == "1 is Prime Number"

def test_zero():
    assert prime_numbers(0) == "0 is Prime Number"

def test_negative_number():
    assert prime_numbers(-5) == "-5 is Prime Number"
