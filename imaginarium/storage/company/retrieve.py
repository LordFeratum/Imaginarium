from imaginarium.storage.company import tablename
from imaginarium.storage.utils import fetchone, fetchall


async def get_company_by_id(request, company_id):
    sql = f"SELECT * FROM {tablename} WHERE id=%(company_id)s"
    params = dict(company_id=company_id)
    async with request.app['pool'].acquire() as conn:
        return await fetchone(conn, sql, params=params, as_dict=True)


async def retrieve_companies(request):
    sql = f"SELECT * FROM {tablename}"
    async with request.app['pool'].acquire() as conn:
        return await fetchall(conn, sql, as_dict=True)
