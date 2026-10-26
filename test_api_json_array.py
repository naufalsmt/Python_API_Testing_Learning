import requests

def test_api_json_array(posts_url):
    response = requests.get(posts_url, timeout=5)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list), f'expected list'
    assert len(data) > 0, f'expected list, got {len(data)}'

    for post in data:
        assert 'id' in post, f'missing id field'
        assert 'userId' in post, f'missing userId field'
        assert 'title' in post, f'missing title field'
        assert post['title'] != '', f'expected title not empty, got empty string'
