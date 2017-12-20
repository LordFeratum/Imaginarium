from imaginarium.views.users.view import (
    get_users,
    get_user,
    insert_user
)


urls = [
    ('GET', '/users', get_users, {'name': 'users:users_list'}),
    ('GET', '/user/{id:\d+}', get_user, {'name': 'users:user_detail'}),
    ('POST', '/user', insert_user, {'name': 'users:user_add'}),
]
