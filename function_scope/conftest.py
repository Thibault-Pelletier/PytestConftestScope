from fixtures import *


def pytest_configure(config):
  config.option.scope = "function"
