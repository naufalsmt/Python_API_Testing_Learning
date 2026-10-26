import requests

def test_send_headers():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get(url, headers=headers, timeout=5)
    assert res.status_code == 200

    content_type = res.headers.get('Content-Type', '')
    assert 'application/json' in content_type.lower(), \
        f'expected "application/json" in {content_type}'

    data = res.json()
    assert data['userId'] == 1