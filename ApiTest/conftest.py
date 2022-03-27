import pytest

from common.yaml_util import clear_yaml


@pytest.fixture(scope="function")

def exe_sql():
    print('q')
    yield
    print('h')

@pytest.fixture(scope="session",autouse=True)
def clear_extract():
    clear_yaml()