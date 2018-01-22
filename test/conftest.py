pytest_plugins = ['helpers_namespace']  # noqa

import pytest


from se_crawler import app


@pytest.fixture(scope='session')
def client():
    with app.app.test_client() as test_client:
        yield test_client
