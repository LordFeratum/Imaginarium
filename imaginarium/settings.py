from os import environ

eget = environ.get


settings = {
    # SERVER
    'IMAGINARIUM_PORT': int(eget('IMAGINARIUM_PORT')),

    # DATABASE
    'DATABASE_NAME': eget('DATABASE_NAME'),
    'DATABASE_USER': eget('DATABASE_USER'),
    'DATABASE_PASS': eget('DATABASE_PASS'),
    'DATABASE_HOST': eget('DATABASE_HOST'),
    'DATABASE_PORT': int(eget('DATABASE_PORT')),
    'DATABASE_ECHO': True if eget('DATABASE_ECHO') == '1' else False,
    'DATABASE_AUTOCOMMIT': True if eget('DATABASE_AUTOCOMMIT') == '1' else False,

    # MIGRATIONS
    'MIGRATIONS_FOLDER': eget('MIGRATIONS_FOLDER'),
}
