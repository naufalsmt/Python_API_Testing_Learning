import pytest


@pytest.fixture
def test_data():
    print('\nPreparing test data...')
    return {
        'amount': 100,
    }

def test_payment_amount(test_data):
    assert test_data['amount'] == 100

def test_payment_positive(test_data):
    assert test_data['amount'] > 0