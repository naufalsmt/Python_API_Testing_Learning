import requests


def test_data_validation():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    req = requests.get(url, timeout=5)
    assert req.status_code == 200

    data = req.json()
    # Validate field is present
    assert 'id' in data, f'"id" not in response'
    assert 'title' in data, f'"title" not in response'
    assert 'userId' in data, f'"userId" not in response'
    assert 'body' in data, f'"body" not in response'

    # Validate data type of fields
    assert isinstance(data['id'], int), f'"id" is not an integer'
    assert isinstance(data['body'], str), f'"body" is not a string'
    assert isinstance(data['title'], str), f'"title" is not a string'
    assert isinstance(data['userId'], int), f'"userId" is not an integer'

    # Validate data value
    assert data['userId'] == 1, f'"userId" is not equal to 1'
    assert data['title'] is not None, '"title" is not set'