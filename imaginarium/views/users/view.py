from datetime import datetime, timedelta

from aiohttp.web import json_response
from jwt import encode as jwt_encode

from imaginarium.storage.user.retrieve import (
    get_user_by_company,
    retrieve_users_by_company,
    user_exists
)

from imaginarium.storage.user.insert import add_user

from imaginarium.views.validation import validate, validate_json
from imaginarium.views.users.validation import UserValidator

from imaginarium.views.utils import login_required

from imaginarium.settings import settings


JWT_SECRET = settings['JWT_SECRET']
JWT_ALGORITHM = settings['JWT_ALGORITHM']
JWT_EXP_DELTA_SECONDS = settings['JWT_EXP_DELTA_SECONDS']


@validate(validator=UserValidator, required=['company_id'])
async def get_users(request, cleaned_data):
    company_id = cleaned_data['company_id']
    users = await retrieve_users_by_company(request, company_id)
    return json_response(users)


@login_required
@validate(validator=UserValidator, required=['company_id', 'id'])
async def get_user(request, cleaned_data):
    company_id = cleaned_data['company_id']
    user_id = cleaned_data['id']
    user = await get_user_by_company(request, company_id, user_id)
    return json_response(user)


@login_required
@validate_json(validator=UserValidator, exclude=['id'])
async def insert_user(request, cleaned_data):
    data = await add_user(request, cleaned_data)
    return json_response({'id': data['lastrowid']}, status=201)


@validate_json(validator=UserValidator, required=['username', 'password'])
async def login(request, cleaned_data):
    username = cleaned_data['username']
    password = cleaned_data['password']
    user = await user_exists(request, username, password)
    payload = {
        'user_id': user['id'],
        'company_id': user['company_id'],
        'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    }
    jwt_token = jwt_encode(payload, JWT_SECRET, JWT_ALGORITHM).decode('utf-8')
    return json_response({'token': jwt_token})
