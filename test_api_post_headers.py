import requests


def test_api_post_headers():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "QA automation test",
        "body": "Testing a POST request",
        "userId": 1
    }

    res = requests.post(url, json=payload, timeout=5)
    assert res.status_code == 201

    content_type = res.request.headers.get('Content-Type', '')
    assert 'application/json' in content_type.lower(), \
        f'Expected "Content-Type: application/json" in {content_type.lower()}'

    data = res.json()
    assert data['userId'] == payload['userId']
    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
