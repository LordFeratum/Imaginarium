from datetime import datetime
from string import hexdigits

from imaginarium.settings import settings


def validate_datetime(value):
    return datetime.strptime(value, settings['IMAGINARIUM_DATETIME_FORMAT'])


def validate_password(value):
    if all(char in hexdigits for char in value):
        return value

    raise ValueError("Incorrect type of password")


def validate_email(value):
    return value


class Validator:
    requirements = {}

    def validate(self, data, required, exclude):
        if required == '__all__':
            required = [
                requirement
                for requirement in self.requirements.keys()
                if requirement not in exclude
            ]

        for required_key in required:
            if required_key not in data:
                raise Exception(f'{required_key} is required')

        return {
            key: self.requirements[key](value)
            for key, value in data.items()
        }


def validate_json(validator=Validator, required="__all__", exclude=None):
    def _wrapper(fnx):
        async def _inner(request, *args, **kwargs):
            data = await request.json()
            cleaned_data = validator.validate(data, required, exclude)
            return await fnx(request, cleaned_data, *args, **kwargs)

        return _inner
    return _wrapper


def validate(validator=Validator, required="__all__", exclude=None):
    def _wrapper(fnx):
        async def _inner(request, *args, **kwargs):
            cleaned_data = validator.validate(
                request.match_info, required, exclude
            )
            return await fnx(request, cleaned_data, *args, **kwargs)

        return _inner
    return _wrapper
