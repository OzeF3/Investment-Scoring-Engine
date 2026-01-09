import pytest

def multiply(a, b):
    return a * b
    

def test_multiply_by_zero_is_always_zero():
    result = multiply(0,5)

    assert result == 0


    
