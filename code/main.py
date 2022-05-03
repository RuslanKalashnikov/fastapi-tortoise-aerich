from fastapi import FastAPI

from code.database import init_tortoise
from code.models.country import Country

app = FastAPI()


@app.get('/')
async def start():
    print(await Country.all())
    return {'message': 'TORTOISE + AERICH'}

init_tortoise(app)
