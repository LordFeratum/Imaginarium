from imaginarium.server import app


def get_arguments():
    return []


def get_help():
    return "Show urls"


def get_name():
    return 'show_urls'


def run(**kwargs):
    for resource in app.router.resources():
        print(resource)
