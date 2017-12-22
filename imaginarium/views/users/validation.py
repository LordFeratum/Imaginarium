from imaginarium.views.validation import (
    Validator, validate_email
)


class UserValidator(Validator):
    requirements = {
        'id': int,
        'name': str,
        'surname': str,
        'company_id': int,
        'enabled': bool,
        'email': validate_email,
        'password': str,
        'username': str
    }
