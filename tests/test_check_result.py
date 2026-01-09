import pytest

def multiply(a, b):
    return a * b

def test_check_multiply_result():
    
    a = 2
    b = 2

    result = multiply(a,b)

    assert result == 4




