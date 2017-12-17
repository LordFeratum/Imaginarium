from aiomysql import create_pool


async def init_database(app=None, config=None):
    if not config:
        config = app['settings']

    pool = await create_pool(
        db=config['DATABASE_NAME'],
        host=config['DATABASE_HOST'],
        port=config['DATABASE_PORT'],
        user=config['DATABASE_USER'],
        password=config['DATABASE_PASS'],
        loop=app.loop
    )

    app['pool'] = pool
    return pool


async def close_database(app=None, config=None):
    app['pool'].close
    await app['pool'].wait_closed()
