import pytest
print("Starting simple pytest scenario")

@pytest.fixture(scope='package')
def greet():
    return 'Hellooo Test Master!'
@pytest.mark.sanitytest
def test_scen1_case1(greet):
    print('test_scen1_case1 startingggg!')
    assert 'hello' == 'hello'
    assert  True
@pytest.mark.negative
def test_scen1_case2():
    print("test_scen1_case1 is started")
    assert 2 == 3, "test_scen1_case1 failed"
    assert False