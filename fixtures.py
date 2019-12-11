import pytest


def determine_scope(fixture_name, config):
  return config.option.scope


@pytest.fixture(scope=determine_scope)
def dyn_scoped_fixture():
  yield
