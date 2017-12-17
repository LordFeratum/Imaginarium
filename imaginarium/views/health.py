from aiohttp import web


class HealthView(web.View):
    async def get(self):
        return web.json_response({'health': 'ok'})
