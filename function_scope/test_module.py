import pytest


@pytest.fixture(scope="function")
def function_fixture(dyn_scoped_fixture):
  yield


def test_passing(function_fixture):
  pass
