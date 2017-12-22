from aiohttp.web import json_response

from imaginarium.storage.user.retrieve import (
    get_user_by_company,
    retrieve_users_by_company
)

from imaginarium.storage.user.insert import add_user

from imaginarium.views.validation import validate, validate_json
from imaginarium.views.users.validation import UserValidator


@validate(validator=UserValidator, required=['company_id'])
async def get_users(request, cleaned_data):
    company_id = cleaned_data['company_id']
    users = await retrieve_users_by_company(request, company_id)
    return json_response(users)


@validate(validator=UserValidator, required=['company_id', 'id'])
async def get_user(request, cleaned_data):
    company_id = cleaned_data['company_id']
    user_id = cleaned_data['id']
    user = await get_user_by_company(request, company_id, user_id)
    return json_response(user)


@validate_json(validator=UserValidator, exclude=['id'])
async def insert_user(request, cleaned_data):
    data = await add_user(request, cleaned_data)
    return json_response({'id': data['lastrowid']}, status=201)
