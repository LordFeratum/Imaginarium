revision = "46def91ce6"
revision_down = "cf6f0fece5"
message = "add username and password to user model"


async def upgrade(connection):
    sql = """
        ALTER TABLE users
            ADD email VARCHAR(100) NOT NULL,
            ADD username VARCHAR(100) NOT NULL,
            ADD password VARCHAR(64) NOT NULL,
            ADD UNIQUE `username_password_unique`(`username`, `password`);
    """
    async with connection.cursor() as cur:
        await cur.execute(sql)


async def downgrade(connection):
    sql = """
        ALTER TABLE users
            DROP INDEX `username_password_unique`,
            DROP COLUMN password,
            DROP COLUMN username,
            DROP COLUMN email;
    """
    async with connection.cursor() as cur:
        await cur.execute(sql)
