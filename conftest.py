import pytest


@pytest.fixture()
def set_up():
    print('Beginning tests')
    yield
    print()
    print('Tests finished')
