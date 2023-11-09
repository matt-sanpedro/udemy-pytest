import pytest
pytestmark = [pytest.mark.smoke, pytest.mark.strtest]

@pytest.mark.sanity
def test_a1():
    assert 4 >= 3
    assert 4 != 3

def test_a2():
    print("Running from a2")
    assert 1
    assert True

@pytest.mark.sanity
@pytest.mark.str
def test_a3():
    assert "abcd" == "ABCD".lower()
    
def test_a4():
    # division operator converts integer to float data type
    assert (3-1)*4/2 == 4.0

def test_a5():
    # divmod(): method takes two numbers as arguments and returns their quotient and remainder in a tuple
    assert 1 in divmod(9,5)
    assert "potato" not in "this is pytest"
    assert 2 in [1,2,4]
    assert [1,2] < [1,2,4]
    assert [1,2,4] == [1,2,4]