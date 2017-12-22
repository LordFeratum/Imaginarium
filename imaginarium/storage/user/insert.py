from imaginarium.storage.user import tablename
from imaginarium.storage.utils import insert, encode_password


async def add_user(request, data):
    data['password'] = encode_password(data['password'])
    async with request.app['pool'].acquire() as conn:
        return await insert(conn, tablename, data)
