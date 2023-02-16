import pytest
print("Starting simple pytest scenario")

#below lines are commented out after transferring the steps to conftest.py file
# @pytest.fixture(scope='package')
# def greet():
#     print("\n--------Set Up!")
#     print('Hellooo Test Master!')
#     yield [2,3,4]
#     print("\n---------Tear Down! ")
#     print("Fixture steps are completed!")


@pytest.mark.regression
@pytest.mark.sanitytest
@pytest.mark.scen1
@pytest.mark.scen1case1
def test_scen1_case1(greet):
    print('\ntest_scen1_case1 starting!')
    print(greet)
    greet.append(5)
    print(greet)
    assert 'hello' == 'hello'


@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.scen1
@pytest.mark.scen1case2
def test_scen1_case2(greet):
    print("\ntest_scen1_case2 is started")
    print(greet)
    greet.append(6)
    print(greet)
    assert 2 == 2, "test_scen1_case2 failed"
