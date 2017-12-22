from aiohttp import web

from imaginarium.storage import init_database, close_database
from imaginarium.urls import urls
from imaginarium.middlewares import auth_middleware
from imaginarium.settings import settings

app = web.Application(middlewares=[auth_middleware])
for method, path, view, kwargs in urls:
    app.router.add_route(method, path, view, **kwargs)

app['settings'] = settings

app.on_startup.append(init_database)
app.on_cleanup.append(close_database)


if __name__ == '__main__':
    web.run_app(app, port=settings['IMAGINARIUM_PORT'])
