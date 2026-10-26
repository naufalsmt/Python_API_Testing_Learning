# find the missing status from the transaction list
def test_api_json_enumerate():
    transactions = [
        {'id': 'TRX1', 'status': 'Approved'},
        {'id': 'TRX2', 'status': 'Approved'},
        {'id': 'TRX3', 'status': 'Declined'},
        {'id': 'TRX4', 'status': 'Approved'},
        {'id': 'TRX5', 'status': 'Declined'},
        {'id': 'TRX6', 'status': 'Approved'},
        {'id': 'TRX7', 'status': 'Approved'},
        {'id': 'TRX8', 'status': 'Approved'},
        {'id': 'TRX9', 'status': 'Approved'},
        {'id': 'TRX10', 'status': ''},
        {'id': 'TRX11', 'status': 'Approved'},
        {'id': 'TRX12', 'status': 'Declined'},
        {'id': 'TRX13', 'status': 'Declined'},
        {'id': 'TRX14', 'status': 'Approved'},
        {'id': 'TRX15', 'status': 'Approved'},
        {'id': 'TRX16', 'status': 'Approved'},
        {'id': 'TRX17', 'status': 'Approved'},
        {'id': 'TRX18', 'status': 'Declined'}
    ]

    for item, transaction in enumerate(transactions, start=1):
        assert transaction['status'] != '', (
            f'Transaction with index {item},',
            f'Id {transaction["id"]}  with status: no status found'
        )


# list the all missing status from the transaction list
def test_api_json_errors():
    transactions = [
        {'id': 'TRX1', 'status': 'Approved'},
        {'id': 'TRX2', 'status': 'Approved'},
        {'id': 'TRX3', 'status': ''},
        {'id': 'TRX4', 'status': 'Approved'},
        {'id': 'TRX5', 'status': 'Declined'},
        {'id': 'TRX6', 'status': 'Approved'},
        {'id': 'TRX7', 'status': ''},
        {'id': 'TRX8', 'status': 'Approved'},
        {'id': 'TRX9', 'status': 'Approved'},
        {'id': 'TRX10', 'status': ''},
        {'id': 'TRX11', 'status': 'Approved'},
        {'id': 'TRX12', 'status': 'Declined'},
        {'id': 'TRX13', 'status': 'Declined'},
        {'id': 'TRX14', 'status': ''},
        {'id': 'TRX15', 'status': 'Approved'},
        {'id': 'TRX16', 'status': 'Approved'},
        {'id': 'TRX17', 'status': ''},
        {'id': 'TRX18', 'status': 'Declined'}
    ]

    errors = []
    for transaction in transactions:
        if transaction['status'] == '':
            errors.append(
                f'Transaction Id {transaction["id"]} found with empty status'
            )
    assert not errors, "\n".join(errors)