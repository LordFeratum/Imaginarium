from aiohttp import web

from imaginarium.storage.company import tablename

from imaginarium.storage.utils import insert


async def add_company(request, data):
    required_fields = ['name']
    if not all((field in required_fields for field in data)):
        raise web.HTTPBadRequest(reason="Invalid fields.")

    async with request.app['pool'].acquire() as conn:
        return await insert(conn, tablename, data)
