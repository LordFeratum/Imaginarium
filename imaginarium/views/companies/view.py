from aiohttp.web import json_response

from imaginarium.storage.company.retrieve import (
    retrieve_companies,
    get_company_by_id,
)

from imaginarium.storage.company.insert import add_company


async def get_companies(request):
    companies = await retrieve_companies(request)
    return json_response(companies)


async def get_company(request):
    company_id = request.match_info['id']
    company = await get_company_by_id(request, company_id)
    if company is None:
        return json_response(None, status=404)

    return json_response(company)


async def insert_company(request):
    json = await request.json()
    result = await add_company(request, json)
    return json_response({'id': result['lastrowid']}, status=201)
