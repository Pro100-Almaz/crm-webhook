import asyncpg
import redis

from app.config import settings


class Database:
    def __init__(self):
        self._pool = None

    async def connect(self):
        self._pool = await asyncpg.create_pool(
            host=settings.POSTGRES_SERVER,
            port=settings.POSTGRES_PORT,
            database=settings.POSTGRES_DB,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            min_size=1, max_size=10, timeout=60)

    async def disconnect(self):
        await self._pool.close()

    async def fetch(self, query: str, *args):
        async with self._pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def fetchrow(self, query: str, *args):
        async with self._pool.acquire() as connection:
            return await connection.fetchrow(query, *args)

    async def execute(self, query: str, *args):
        async with self._pool.acquire() as connection:
            return await connection.execute(query, *args)


# class RedisDatabase:
#     def __init__(self):
#         self.r = redis.Redis(host="localhost", port=6379, db=0)


database = Database()
# redis_database = RedisDatabase()
