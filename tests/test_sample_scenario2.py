import pytest
print("Starting simple pytest scenario")

@pytest.mark.sanitytest
def test_greet_user(greet):
    print('hello user!')
    assert 'hello' == 'hello'

@pytest.mark.negative
def test_scen2_case2():
    print("test_scen2_case2 is started")
    assert 2 ==3, "test_scen2_case1 failed"
    assert False