from uuid import uuid1
from os import walk, path
from importlib import import_module
from functools import reduce
from copy import deepcopy

from imaginarium.settings import settings

from imaginarium.storage.utils import (
    create_database_connection, execute, fetchone
)


def _get_identifier():
    return str(uuid1()).replace('-', '')[:10]


async def _create_migrate_table(loop):
    async with create_database_connection(settings, loop=loop) as conn:
        sql = """
            CREATE TABLE IF NOT EXISTS migrations (
                migration_id CHAR(200)
            );
        """
        await execute(conn, sql)


async def _get_current_migration(loop):
    async with create_database_connection(settings, loop=loop) as conn:
            sql = "SELECT migration_id FROM migrations"
            res = await fetchone(conn, sql)
            if res is None:
                return None

            return res[0]


def _get_migration_files():
    folder = settings['MIGRATIONS_FOLDER']
    for dirpath, _, filenames in walk(folder):
        for filename in filenames:
            if filename.endswith('.py') and filename != '__init__.py':
                yield path.join(dirpath, filename)\
                    .replace('/', '.')\
                    .replace('.py', '')


async def _get_migrations_tree(loop):
    def _format_tree(tree, migration_file):
        migration = import_module(migration_file)
        if migration.revision_down is None:
            tree['first_revision'] = migration.revision

        tree.setdefault('revisions', {})
        tree['revisions'][migration.revision] = {
            'down': migration.revision_down,
            'up': None,
            'upgrade': migration.upgrade,
            'downgrade': migration.downgrade
        }
        return tree

    def _loop_upside_tree(tree):
        _tree = deepcopy(tree)
        for current, info in _tree.get('revisions', {}).items():
            current_down = info['down']
            if current_down is not None:
                _tree['revisions'][current_down]['up'] = current
        return _tree

    tree = reduce(_format_tree, _get_migration_files(), {})
    tree['current'] = await _get_current_migration(loop)
    tree = _loop_upside_tree(tree)
    return tree


def _get_migration_filename(migration_id, message):
    migrations_path = settings['MIGRATIONS_FOLDER']
    params = {
        'id': migration_id,
        'msg': message.replace(' ', '_').lower()
    }
    filename = "{id}_{msg}.py".format(**params)
    return path.join(migrations_path, filename)


def _save_migration_file(migration_id, down_revision, message):
    migration_file = _get_migration_filename(migration_id, message)
    d_revision = "None"
    if down_revision is not None:
        d_revision = '"{}"'.format(down_revision)

    params = {
        'revision': migration_id,
        'down_revision': d_revision,
        'message': message
    }
    with open(migration_file, 'w') as fp:
        fp.write((
            'revision = "{revision}"\n'
            'revision_down = {down_revision}\n'
            'message = "{message}"\n\n\n'
            'async def upgrade(connection):\n'
            '\tpass\n\n\n'
            'async def downgrade(connection):\n'
            '\tpass'
        ).format(**params))

    return migration_file


async def _update_migration_revision(loop, current_revision, new_revision):
    async with create_database_connection(settings, loop=loop) as conn:
        if current_revision is None:
            sql = """
                INSERT INTO migrations (migration_id)
                VALUES ("{}");
            """.format(new_revision)

        else:
            sql = """
                UPDATE migrations SET
                    migration_id = "{}"
                WHERE migration_id = "{}";
            """.format(new_revision, current_revision)

        await execute(conn, sql)


async def _create(loop, message, migrations_tree):
    migration_id = _get_identifier()
    migration_file = _save_migration_file(migration_id,
                                          migrations_tree['current'],
                                          message)
    print("Created migration file '{}'".format(migration_file))


async def _apply(loop, migrations_tree):
    pass


def get_arguments():
    return [
        [
            ('--create', '-c'),
            dict(default=False, action='store_true')
        ],
        [
            ('--upgrade', '-u'),
            dict(default=False, action='store_true')
        ],
        [
            ('--message', '-m'),
            dict(type=str, default='')
        ]
    ]


def get_help():
    return "Create a migration file"


def get_name():
    return 'migrate'


async def run(loop=None, **kwargs):
    await _create_migrate_table(loop)
    migrations_tree = await _get_migrations_tree(loop)
    from pprint import pprint
    pprint(migrations_tree)
    if 'create' in kwargs:
        await _create(loop, kwargs['message'], migrations_tree)
