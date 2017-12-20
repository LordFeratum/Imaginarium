from imaginarium.views.health.urls import urls as health_urls
from imaginarium.views.users.urls import urls as users_urls
from imaginarium.views.companies.urls import urls as companies_urls


urls = [
    *health_urls,
    *users_urls,
    *companies_urls,
]
