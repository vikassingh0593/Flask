from square import get_square

# this is one of my test case.
def test_sq():
    x = 5
    res = get_square(5)
    assert res == 25 # assert -> used for test.
    assert get_square(3) == 9