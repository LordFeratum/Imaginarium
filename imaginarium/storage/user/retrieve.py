from imaginarium.storage.company import tablename
from imaginarium.storage.utils import (
    fetchone,
    fetchall,
    encode_password
)


async def get_user_by_company(request, company_id, user_id):
    sql = f"""
        SELECT * FROM {tablename}
        WHERE id=%(user_id)s
          AND company_id=%(company_id)s
    """
    params = {
        'user_id': user_id,
        'company_id': company_id
    }
    async with request.app['pool'].acquire() as conn:
        return await fetchone(conn, sql, params=params, as_dict=True)


async def user_exists(request, username, password):
    sql = f"""
        SELECT id FROM {tablename}
        WHERE username = %(username)s
          AND password = %(password)s
    """
    attrs = {
        'username': username,
        'password': encode_password(password)
    }
    async with request.app['pool'].acquire() as conn:
        return await fetchone(conn, sql, params=attrs)


async def retrieve_users_by_company(request, company_id):
    sql = f"SELECT * FROM {tablename} WHERE company_id = %(company_id)s"
    params = dict(company_id=company_id)
    async with request.app['pool'].acquire() as conn:
        return await fetchall(conn, sql, params=params, as_dict=True)
