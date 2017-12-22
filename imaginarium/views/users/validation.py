from imaginarium.views.validation import (
    Validator, validate_password, validate_email
)


class UserValidator(Validator):
    requirements = {
        'id': int,
        'name': str,
        'surname': str,
        'company_id': int,
        'enabled': bool,
        'email': validate_email,
        'password': validate_password,
        'username': str
    }
