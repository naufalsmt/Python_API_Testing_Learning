import requests


def test_posts_api(base_url):
    url = f'{base_url}/posts/1'
    response = requests.get(url)
    assert response.status_code == 200, \
        f'expected 200, got {response.status_code}'

    data = response.json()
    assert data['id'] == 1
    assert data['title'] != ''