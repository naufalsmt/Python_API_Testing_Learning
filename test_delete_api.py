import requests

def test_delete_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    res = requests.delete(url, timeout=5)
    assert res.status_code == 200, \
        f'expected 200, got {res.status_code}'

    data = res.json()
    assert data == {}, \
        f'expected empty dictionary, but got {data}'