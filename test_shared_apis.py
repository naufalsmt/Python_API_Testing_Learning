import requests


def test_first_post(posts_url):
    res = requests.get(
        f'{posts_url}/1',
        timeout=5
    )
    assert res.status_code == 200, f'expected 200 status code, got {res.status_code}'

    data = res.json()
    assert data['id'] == 1


def test_second_post(posts_url):
    res = requests.get(
        f'{posts_url}/2',
        timeout=5
    )
    assert res.status_code == 200, f'expected 200 status code, got {res.status_code}'

    data = res.json()
    assert data['id'] == 2