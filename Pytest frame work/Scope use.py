from urllib import request

import pytest
class Test:
    @pytest.fixture(scope='function',autouse=True)
    def setup(self):
        print("my fixture is called")
        yield
        print("my fixture is closed")

    def test_method1(self):
     print("Test_method-1 is called")
    def test_method2(self):
     print("test_method-2 is called")
    def test_method3(self):
     print("test_method-3 is called")

