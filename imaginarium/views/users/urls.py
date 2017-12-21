from imaginarium.views.users.view import (
    get_users,
    get_user,
    insert_user
)


urls = [
    ('GET', '/company/{company_id:\d+}/users', get_users,
     {'name': 'users:users_list'}),
    ('GET', '/company/{company_id:\d+}/user/{id:\d+}', get_user,
     {'name': 'users:user_detail'}),
    ('POST', '/company/{company_id:\d+}/user', insert_user,
     {'name': 'users:user_add'}),
]
