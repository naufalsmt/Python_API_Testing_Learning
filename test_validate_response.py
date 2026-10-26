import requests


def test_validate_response(posts_url):
    response = requests.get(
        f'{posts_url}/1',
        timeout=5
    )
    assert response.status_code == 200

    data = response.json()

    res_list = [
        'id', 'title', 'userId', 'body'
    ]

    for item in res_list:
        assert item in data, \
            f'{item} not in data'

    assert isinstance(data['id'], int)
    assert isinstance(data['title'], str)
    assert isinstance(data['userId'], int)
    assert isinstance(data['body'], str)