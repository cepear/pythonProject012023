# This is shared fixture between modules
import pytest


@pytest.fixture(scope='module')
def greet():
    print("\n--------Set Up!")
    print('Hellooo Test Master!')
    yield [2,3,4]
    print("\n---------Tear Down! ")
    print("Fixture steps are completed!")