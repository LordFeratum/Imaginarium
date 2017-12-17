from aiohttp import web

from imaginarium.storage import init_database, close_database
from imaginarium.urls import urls
from imaginarium.settings import settings

app = web.Application()
for method, path, view, kwargs in urls:
    app.router.add_route(method, path, view, **kwargs)

app['settings'] = settings

app.on_startup.append(init_database)
app.on_cleanup.append(close_database)
