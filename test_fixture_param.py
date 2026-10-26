import pytest
import requests


@pytest.mark.parametrize(
    'user_id',
    [1, 2, 3],
    ids=['user1', 'user2', 'user3']
)
def test_users(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {'userId': user_id}
    res = requests.get(url, params=params, timeout=5)
    assert res.status_code == 200

    data = res.json()
    assert len(data) > 0, \
        f'no posts return for user, {user_id}'
    for post in data:
        assert post['userId'] == user_id, \
            f'expected {user_id}, got {post["userId"]}'
