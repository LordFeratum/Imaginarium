revision = "a6d2d466e5"
revision_down = None
message = "create company model"


async def upgrade(connection):
    sql = """
        CREATE TABLE companies (
            id MEDIUMINT NOT NULL AUTO_INCREMENT,
            name CHAR(200) NOT NULL,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8 COLLATE utf8_unicode_ci;
    """
    async with connection.cursor() as cur:
        await cur.execute(sql)


async def downgrade(connection):
    sql = "DROP TABLE companies"
    async with connection.cursor() as cur:
        await cur.execute(sql)

