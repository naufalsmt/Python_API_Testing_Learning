def test_simulate_nested_data():
    data = {
        'id': 1,
        'address': {
            'city': 'Ajman'
        }
    }

    adr = data.get('address', {})
    cty = adr.get('city')

    assert cty is not None, f'city is empty dictionary'
    assert cty != '', f'city field is empty'
    assert cty == 'Ajman', f'city is {cty}'

