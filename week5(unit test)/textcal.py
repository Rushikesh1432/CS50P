import pytest
from calculator import square


#defining more  test cases helps to find the mistake we did
 
#pytest runs all test cases even one test fail
def main():
    test_negative()
    test_positive()
    test_zero()


def test_positive():
    assert square(2)==4
    assert square(3)==9



def test_negative():    
    assert square(-2)==4
    assert square(-8)==64

def test_zero():
    assert square(0)==0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
        #This code 
if __name__=="__main__":
    main()