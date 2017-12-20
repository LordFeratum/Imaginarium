from aiohttp.web import Response, json_response


async def get_users(request):
    return json_response({'users': []})


async def get_user(request):
    return json_response({'user': None})


async def insert_user(request):
    return Response(status=201)
