import requests


def test_token_api(base_url, bearer_token):
    res = requests.get(
        f'{base_url}/profile',
        # headers = bearer_token,
        timeout = 5,
    )
    assert res.status_code == 401
