from pymongo import MongoClient
from api.settings import Settings
 
config = Settings()

async def get_colletion(name:str):
    client = MongoClient(config.mongoUri)

    assert client

    database = getattr(client,config.mongoDatabase)

    