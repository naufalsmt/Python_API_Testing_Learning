import requests


def test_try_exception_api(posts_url):
    try:
        response = requests.get(
            f'{posts_url}/1',
            timeout=5,
        )
        assert response.status_code == 200, \
            f'expected 200, got {response.status_code}'
    except requests.exceptions.Timeout:
        print("API request failed due to timed out")
        raise