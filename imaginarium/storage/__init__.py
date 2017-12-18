from imaginarium.storage.utils import create_database_pool


async def init_database(app=None, config=None):
    if not config:
        config = app['settings']

    pool = await create_database_pool(config, loop=app.loop)
    app['pool'] = pool

    return pool


async def close_database(app=None, config=None):
    app['pool'].close
    await app['pool'].wait_closed()
