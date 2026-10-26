import pytest


@pytest.fixture
def test_data():
    print('\nPreparing test data...')
    data = {
        "amount" : 100,
        "currency" : "AED"
    }

    yield data
    print('\nTearing down test data...')

def test_amount(test_data):
    assert test_data['amount'] == 100

def test_currency(test_data):
    assert test_data['currency'] == 'AED'