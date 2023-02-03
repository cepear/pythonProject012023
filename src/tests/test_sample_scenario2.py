import pytest
print("Starting simple pytest scenario")


@pytest.mark.regression
@pytest.mark.sanitytest
def test_greet_user(greet):
    print('\n scenario 2 case 1 starting')
    assert True

@pytest.mark.regression
@pytest.mark.negative
def test_scen2_case2(greet):
    print("\n scenario 2 case2 is started")
    assert False

