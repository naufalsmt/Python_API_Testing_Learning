import requests


def test_nested_json(users_url):
    res = requests.get(
        f'{users_url}/1',
        timeout=5,
    )
    assert res.status_code == 200

    data = res.json()

    assert 'id' in data
    assert 'address' in data

    assert isinstance(data['address'], dict)
    assert 'city' in data['address']
    assert data['address']['city'] != '', \
        f'expected city but got city={data["address"]["city"]}'