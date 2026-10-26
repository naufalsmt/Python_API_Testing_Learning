import requests
import pytest

@pytest.fixture
def api_url():
    return 'https://jsonplaceholder.typicode.com/users/1'

def test_get_api(api_url):
    res = requests.get(api_url, timeout=5)
    assert res.status_code == 200

    data = res.json()
    assert data['name'] == 'Leanne Graham'

def test_name_change_api(api_url):
    payload = {
        'name': 'Alex Smith'
    }
    res = requests.patch(api_url, json=payload, timeout=5)
    assert res.status_code == 200

    data = res.json()
    assert data['name'] == payload['name']