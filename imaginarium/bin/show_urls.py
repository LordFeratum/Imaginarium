from imaginarium.server import app


def _green_bold(value):
    return '\33[1;32m{}\033[0m'.format(value)


def _white_bold(value):
    return '\33[1;39m{}\033[0m'.format(value)


def _blue(value):
    return '\33[0;34m{}\033[0m'.format(value)


def _gold(value):
    return '\33[0;33m{}\033[0m'.format(value)


def _red(value):
    return '\33[0;31m{}\033[0m'.format(value)


def _prettify(method, path, name, module, function):
    method = _white_bold(method)
    path = _green_bold(path)
    name = _red(name)
    module = _gold(module)
    function = _blue(function)

    print(f'{method}\t{path}\t{module}.{function}\t{name}')


def get_arguments():
    return []


def get_help():
    return "Show urls"


def get_name():
    return 'show_urls'


def run(**kwargs):
    for resource in app.router.resources():
        for route in resource._routes:
            method = route.method
            path = route.get_info().get('path', route.get_info().get('formatter'))
            name = route.name
            module = route._handler.__module__
            function = route._handler.__name__

            _prettify(method, path, name, module, function)
