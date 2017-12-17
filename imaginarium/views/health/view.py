from aiohttp.web import json_response


async def get_health_status(request):
    return json_response({'health': 'ok'})
