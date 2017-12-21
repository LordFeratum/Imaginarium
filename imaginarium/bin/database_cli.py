from mycli.main import cli

from imaginarium.settings import settings


def get_arguments():
    return []


def get_help():
    return "Opens a cli database interface"


def get_name():
    return 'database_cli'


def run(**kwargs):
    host = settings['DATABASE_HOST']
    port = settings['DATABASE_PORT']
    name = settings['DATABASE_NAME']
    user = settings['DATABASE_USER']
    pwd = settings['DATABASE_PASS']
    db_name = settings['DATABASE_NAME']

    cli('', user, host, port, None, pwd, db_name, False, '>', )
