from aiohttp.web import middleware, json_response

from  jwt import (
    decode as jwt_decode,
    DecodeError,
    ExpiredSignatureError
)

from imaginarium.storage.user.retrieve import get_user_by_company

from imaginarium.settings import settings


@middleware
async def auth_middleware(request, handler):
    request.user = None
    jwt_token = request.headers.get('authorization', None)
    if jwt_token:
        try:
            payload = jwt_decode(jwt_token, settings['JWT_SECRET'],
                                 algorithms=[settings['JWT_ALGORITHM']])

        except (DecodeError, ExpiredSignatureError):
            msg = {'message': 'Invalid Token'}
            return json_response(msg, status=400)

        company_id = payload['company_id']
        user_id = payload['user_id']
        request.user = await get_user_by_company(request, company_id, user_id)

    return await handler(request)
