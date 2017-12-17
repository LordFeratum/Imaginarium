from aiohttp import web

from imaginarium import settings
from imaginarium.urls import urls


app = web.Application()
for path, view in urls:
    app.router.add_route('*', path, view)


if __name__ == '__main__':
    port = settings.IMAGINARIUM_PORT
    web.run_app(app, port=port)
