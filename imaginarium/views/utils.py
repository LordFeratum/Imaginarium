from functools import wraps

from aiohttp import web


def login_required(fnx):
    @wraps(fnx)
    async def _inner(request, *args, **kwargs):
        if request.user is None:
            raise web.HTTPForbidden()

        return await fnx(request, *args, **kwargs)

    return _inner
