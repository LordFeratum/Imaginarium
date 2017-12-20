from imaginarium.views.companies.view import (
    get_companies,
    get_company,
    insert_company
)


urls = [
    ('GET', '/companies', get_companies,
     {'name': 'companies:companies_list'}),
    ('GET', '/company/{id:\d+}', get_company,
     {'name': 'companies:company_detail'}),
    ('POST', '/company', insert_company,
     {'name': 'companies:company_add'}),
]
