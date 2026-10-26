import requests


def test_api_header_validation():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    res = requests.get(url, timeout=5)
    assert res.status_code == 200

    content_type = res.headers.get('Content-Type', '')
    assert 'application/json' in content_type.lower(), \
        f'expected application/json content type, but got {content_type}'

    data = res.json()
    assert data['userId'] == 1, f'expected "userId" to be equal to "1"'