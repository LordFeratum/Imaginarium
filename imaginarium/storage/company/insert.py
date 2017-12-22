from imaginarium.storage.company import tablename
from imaginarium.storage.utils import insert


async def add_company(request, data):
    async with request.app['pool'].acquire() as conn:
        return await insert(conn, tablename, data)
