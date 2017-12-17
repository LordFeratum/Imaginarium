from os import environ

eget = environ.get


IMAGINARIUM_PORT = int(eget('IMAGINARIUM_PORT'))
