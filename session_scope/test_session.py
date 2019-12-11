import pytest


@pytest.fixture(scope="session")
def session_fixture(dyn_scoped_fixture):
  yield


def test_passing(session_fixture):
  pass
