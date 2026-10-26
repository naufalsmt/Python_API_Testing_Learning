import pytest
import requests

@pytest.mark.parametrize(
    'post_id, exp_status',
    [
        (1, 200),
        (99999, 404),
    ],
    ids=['post1', 'post99999']
)
def test_fixture_combine_negative(posts_url, post_id, exp_status):
    response = requests.get(
        f'{posts_url}/{post_id}',
        timeout=5
    )
    assert response.status_code == exp_status, \
        f'expected {exp_status} for post {post_id}, got {response.status_code}'