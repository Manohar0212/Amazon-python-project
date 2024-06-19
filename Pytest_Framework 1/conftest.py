import pytest


@pytest.fixture( scope='function', autouse=True)
def setup():
    print("conftest fixture is called")
    yield
    print("conftest fixture closed")


