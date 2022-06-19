from pymongo import MongoClient

import config as cf


def create_database():
    client = MongoClient(cf.CONNECTION_STRING)
    return client[cf.DATABASE]
