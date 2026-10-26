import requests
import pytest


@pytest.mark.parametrize(
    'post_id',
    [1, 2, 3, 99999],
    ids=['post1', 'post2', 'post3', 'post99999']
)
def test_fixture_combine(posts_url, post_id):
    res = requests.get(
        f'{posts_url}/{post_id}',
        timeout=5)
    assert res.status_code == 200, \
        f'expected 200 status code for post_id {post_id}, got {res.status_code}'

    data = res.json()
    assert data['id'] == post_id, f'expected postId {post_id}, got {data.get("postId")}'
    assert data['title'] != '', \
        f'expected "title" to not be empty, got "{data['title']}"'