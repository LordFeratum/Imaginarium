from imaginarium.views.validation import (
    Validator,
)


class CompanyValidator(Validator):
    requirements = {
        'id': int,
        'name': str,
    }
