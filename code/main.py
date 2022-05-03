import asyncio
from fastapi import FastAPI

from code import database
from code.models.country import Country

app = FastAPI()


@app.get("/")
async def start():
    print(await Country.all())
    return {'message': 'TORTOISE + AERICH'}


asyncio.create_task(database.init())
asyncio.ensure_future(database.init())
