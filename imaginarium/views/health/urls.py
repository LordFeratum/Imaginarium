from imaginarium.views.health.view import get_health_status


urls = [
    ('GET', '/health', get_health_status, {'name': 'health:status'})
]
