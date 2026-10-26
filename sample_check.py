def validate_status(status):
    allowed_status = [
        'Pending',
        'Processing'
    ]
    return status in allowed_status

print(validate_status('Pending'))
print(validate_status('Processing'))
print(validate_status('Approved'))
print(validate_status('Rejected'))