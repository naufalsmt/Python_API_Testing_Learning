import pytest

def simulate_api(token):
    if token == 'valid_token':
        return {
            'status_code' : 200,
            'message' : 'success'
        }
    return {
        'status_code' : 401,
        'message' : 'invalid token'
    }

@pytest.mark.parametrize(
    'token, status_code, exp_msg',
    [
        ('valid_token', 200, 'success'),
        ('invalid_token', 401, 'invalid token'),
        ('', 401, 'invalid token'),
    ],
    ids = [
        'valid_token',
        'invalid_token',
        'missing_token'
    ]
)
def test_token_api(token, status_code, exp_msg):
    res = simulate_api(token)
    assert res['status_code'] == status_code
    assert res['message'] == exp_msg
