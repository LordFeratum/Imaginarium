from imaginarium.views.validation import (
    Validator,
)


class UserValidator(Validator):
    requirements = {
        'id': int,
        'name': str,
        'surname': str,
        'company_id': int,
        'enabled': bool,
        'email': str,
        'password': str,
        'username': str
    }
