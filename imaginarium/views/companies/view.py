from aiohttp.web import json_response

from imaginarium.storage.company.retrieve import (
    retrieve_companies,
    get_company_by_id,
)

from imaginarium.storage.company.insert import add_company

from imaginarium.views.validation import validate, validate_json
from imaginarium.views.companies.validation import CompanyValidator


async def get_companies(request):
    companies = await retrieve_companies(request)
    return json_response(companies)


@validate(validator=CompanyValidator, required=['id'])
async def get_company(request, cleaned_data):
    company_id = cleaned_data['id']
    company = await get_company_by_id(request, company_id)
    if company is None:
        return json_response(None, status=404)

    return json_response(company)


@validate_json(validator=CompanyValidator, required="__all__", exclude=['id'])
async def insert_company(request, cleaned_data):
    result = await add_company(request, cleaned_data)
    return json_response({'id': result['lastrowid']}, status=201)
