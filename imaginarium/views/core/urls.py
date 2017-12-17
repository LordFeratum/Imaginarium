from imaginarium.views.core.view import get_users


urls = [
    ('GET', '/user', get_users, {'name': 'core:users_list'})
]
