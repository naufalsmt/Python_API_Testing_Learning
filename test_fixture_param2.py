import pytest
import requests

@pytest.mark.parametrize(
    "user_id",
    [1,1,2],
    ids = [1,2,3]
)

def test_post_apis(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    res = requests.get(url, params=params, timeout=5)
    assert res.status_code == 200
    data = res.json()
    assert len(data) > 0
    for post in data:
        assert post['userId'] == user_id


def test_api_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    params = {'userId': 1}
    res = requests.get(url, params=params, timeout=10)
    assert res.status_code == 200

    data = res.json()
    assert len(data) > 0
    for post in data:
        assert post['userId'] == 1