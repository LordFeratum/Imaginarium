from aiohttp.web import json_response


async def get_users(request):
    return json_response({'users': []})
