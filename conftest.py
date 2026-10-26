import pytest


@pytest.fixture
def base_url():
    return 'https://jsonplaceholder.typicode.com'


@pytest.fixture
def posts_url(base_url):
    return f'{base_url}/posts'


@pytest.fixture
def users_url(base_url):
    return f'{base_url}/users'


@pytest.fixture
def auth_token():
    return {
        'authorization': 'Bearer TEST_TOKEN',
        'Accept': 'application/json'
    }