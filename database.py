from pymongo import MongoClient

import config as cf


def create_database():
    client = MongoClient(cf.CLIENT_LOGIN)
    return client[cf.DATABASE]
