import pytest
import requests


def test_http_error(posts_url):
    res = requests.get(
        f'{posts_url}/1',
        timeout=5,
    )
    res.raise_for_status()

    assert res.status_code == 200

    data = res.json()
    assert data['id'] == 1

