from imaginarium.server import app


def _green(value):
    return '\33[0;32m{}\033[0m'.format(value)


def _red(value):
    return '\33[0;31m{}\033[0m'.format(value)


def get_arguments():
    return []


def get_help():
    return "Show urls"


def get_name():
    return 'show_urls'


def run(**kwargs):
    for resource in app.router.resources():
        path = _green(resource.get_info().get('path', resource.get_info().get('formatter')))
        name = _red(resource._name)
        print('{}  {}'.format(path, name))

