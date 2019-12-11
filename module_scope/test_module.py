import pytest


@pytest.fixture(scope="module")
def module_fixture(dyn_scoped_fixture):
  yield


def test_passing(module_fixture):
  pass
