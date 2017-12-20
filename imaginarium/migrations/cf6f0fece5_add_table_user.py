revision = "cf6f0fece5"
revision_down = "a6d2d466e5"
message = "add table user"


async def upgrade(connection):
    sql = """
        CREATE TABLE users (
            id MEDIUMINT NOT NULL AUTO_INCREMENT,
            name CHAR(200) NOT NULL,
            surname CHAR(200) NULL,
            company_id MEDIUMINT NOT NULL,
            enabled TINYINT(1) DEFAULT 1,

            INDEX company_id_idx (company_id),
            FOREIGN KEY (company_id)
                REFERENCES companies(id)
                ON DELETE CASCADE,

            PRIMARY KEY (id)
        ) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8 COLLATE utf8_unicode_ci;
    """
    async with connection.cursor() as cur:
        await cur.execute(sql)


async def downgrade(connection):
    sql = "DROP TABLE users;"
    async with connection.cursor() as cur:
        await cur.execute(sql)

