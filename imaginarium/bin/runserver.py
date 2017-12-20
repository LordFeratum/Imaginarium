from imaginarium.server import app


def get_arguments():
    return [
        [
            ('--port', '-p'),
            dict(type=int, required=False)
        ]
    ]


def get_help():
    return "Run the server"


def get_name():
    return 'runserver'


async def run(loop=None, **kwargs):
    port = kwargs.get('port', app['settings']['IMAGINARIUM_PORT'])
    handler = app.make_handler()
    f = loop.create_server(handler, '0.0.0.0', port)
    srv = await f
    print("Serving on 0.0.0.0:{}".format(port))
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    finally:
        srv.close()
        await srv.wait_closed()
        await app.shutdown()
        await handler.shutdown(60.0)
        await app.cleanup()
