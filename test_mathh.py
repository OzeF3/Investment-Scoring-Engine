
import pytest
from math_utl import divide

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
