import pytest
import requests

@pytest.fixture
def api_session():
    print('\nPreparing API session...')
    session = requests.Session()
    yield session
    print('\nClosing API session...')
    session.close()


def test_api_posts(api_session):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    res = api_session.get(url, timeout=5)
    assert res.status_code == 200
    data = res.json()
    assert data['id'] == 2

def test_api_users(api_session):
    url = "https://jsonplaceholder.typicode.com/users/1"
    res = api_session.get(url, timeout=5)
    assert res.status_code == 200
    data = res.json()
    assert data['id'] == 1