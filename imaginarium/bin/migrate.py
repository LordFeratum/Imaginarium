from imaginarium.server import app


def get_arguments():
    return []


def get_help():
    return "Create a migration file"


def get_name():
    return 'migrate'


async def run(loop=None, **kwargs):
    print(loop)
    print(app['settings'])
