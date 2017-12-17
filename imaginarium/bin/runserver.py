from aiohttp import web

from imaginarium.server import app


def get_arguments():
    return [
        {
            'name': '--port',
            'small_name': '-p',
            'type': int,
            'required': False
        }
    ]


def get_help():
    return "Run the server"


def get_name():
    return 'runserver'


def run(**kwargs):
    port = kwargs.get('port', app['settings']['IMAGINARIUM_PORT'])
    web.run_app(app, port=port)
