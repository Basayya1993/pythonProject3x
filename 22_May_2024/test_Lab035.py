import pytest
import allure

def test_addition():
    assert 1+2 == 3

def test_addition1():
    assert  2+3 == 5


@pytest.mark.smoke
def test_sub():
    assert 4-1 != 3



