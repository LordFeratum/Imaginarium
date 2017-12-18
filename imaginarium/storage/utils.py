from asyncio import get_event_loop

from aiomysql import connect, create_pool, DictCursor


async def create_database_pool(config, loop=None):
    _loop = loop or get_event_loop()
    return await create_pool(
        db=config['DATABASE_NAME'],
        host=config['DATABASE_HOST'],
        port=config['DATABASE_PORT'],
        user=config['DATABASE_USER'],
        password=config['DATABASE_PASS'],
        echo=config['DATABASE_ECHO'],
        autocommit=config['DATABASE_AUTOCOMMIT'],
        loop=_loop
    )


class create_database_connection:
    def __init__(self, config, loop=None):
        self._config = config
        self._loop = loop or get_event_loop()
        self._connection = None

    async def __aenter__(self):
        self._connection = await connect(
            db=self._config['DATABASE_NAME'],
            host=self._config['DATABASE_HOST'],
            port=self._config['DATABASE_PORT'],
            user=self._config['DATABASE_USER'],
            password=self._config['DATABASE_PASS'],
            echo=self._config['DATABASE_ECHO'],
            autocommit=self._config['DATABASE_AUTOCOMMIT'],
            loop=self._loop
        )
        return self._connection

    async def __aexit__(self, exc, exc_n, traceback):
        self._connection.close()
        if exc is None:
            return True

        return False


async def execute(connection, sql, params=None):
    async with connection.cursor() as cur:
        await cur.execute(sql, args=params)
        return {
            'rowcount': cur.rowcount,
            'lastrowid': cur.lastrowid
        }


async def fetch(connection, sql, params, as_one, as_dict):
    cursor_class = DictCursor if as_dict else None
    async with connection.cursor(cursor_class) as cur:
        await cur.execute(sql, args=params)
        if as_one:
            return await cur.fetchone()

        return await cur.fetchall()


async def fetchone(connection, sql, params=None, as_dict=False):
    return await fetch(connection, sql, params, True, as_dict)


async def fetchall(connection, sql, params=None, as_dict=False):
    return await fetch(connection, sql, params, False, as_dict)
