import pytest

def validate_status(status):
    allowed_status = [
        'Pending',
        'Processing'
    ]
    return status in allowed_status

@pytest.mark.parametrize(
    'status, exp_status',
    [
        ('Pending', True),
        ('Processing', True),
        ('Undefined', False),
        ('', False)
     ],
    ids=[
        'Pending status',
        'Processing status',
        'Undefined status',
        'empty status'
    ]
)
def test_validate_status(status, exp_status):
    assert validate_status(status) == exp_status, \
        f'status "{status}" found {exp_status}'