import pytest

def adicion(num1:int,num2:int)->int:
    return num1 + num2

def test_adicion():
    assert adicion(3,4) == 7
    
def test_adicion_with_strings_fail():
    with pytest.raises(TypeError):
        adicion("3",5)