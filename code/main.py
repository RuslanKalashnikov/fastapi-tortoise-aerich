from fastapi import FastAPI

from code import database

app = FastAPI()


@app.get("/")
async def start():
    return {'message': 'TORTOISE + AERICH'}


database.init()
