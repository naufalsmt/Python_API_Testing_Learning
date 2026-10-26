def test_api_allowed():
    transactions = [
        {'id': 'TRX1', 'status': 'Pending'},
        {'id': 'TRX2', 'status': 'Processing'},
        {'id': 'TRX3', 'status': 'Approved'},
        {'id': 'TRX4', 'status': 'Declined'},
        {'id': 'TRX5', 'status': 'UNDEFINED'},
        {'id': 'TRX6', 'status': 'Pending'},
        {'id': 'TRX7', 'status': 'UNDEFINED'},
        {'id': 'TRX8', 'status': 'Processing'}
    ]
    allowed_status = [
        'Pending', 'Processing', 'Approved', 'Declined'
    ]

    errors = []
    for transaction in transactions:
        status = transaction.get('status')
        if status not in allowed_status:
            errors.append(
                f'transaction id {transaction["id"]}: status "{status}"'
            )

    assert not errors, '\n'.join(errors)