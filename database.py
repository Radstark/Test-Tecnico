from pydantic import BaseModel
from pymongo import MongoClient

import config as cf


def create_database():
    client = MongoClient(cf.CONNECTION_STRING)
    return client[cf.DATABASE]


class IngestionData(BaseModel):
    key: int
    payload: str


class RetrievalData(BaseModel):
    Date_from: str
    Date_to: str
