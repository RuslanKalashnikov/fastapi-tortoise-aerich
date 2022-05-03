from tortoise import Tortoise

from code import settings


async def init():
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={
            'models': ['code.models', 'aerich.models'],
        },
    )
