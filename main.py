import datetime
import random
import time
from typing import Dict, Union

from dateutil import parser as date_parser
from fastapi import FastAPI
from pydantic import BaseModel

import config as cf
from database import create_database

app = FastAPI()

database = create_database()


class IngestionData(BaseModel):
    key: int
    payload: str


class RetrievalData(BaseModel):
    Date_from: str
    Date_to: str


@app.post(cf.URL_INGEST)
def ingest(data: IngestionData):
    """
    Accepts a request and inserts its data in MongoDB with a fixed date. Response code is randomly 500 10% of the time,
    200 all other times. Takes anywhere between 10 ms and 50 ms, at random.
    :param data: class containing an integer key and a string payload.
    """

    print(data)

    beginning = time.time()
    creation_datetime = datetime.datetime.now()
    key = data.key
    payload = data.payload

    if random.randrange(1, 11) == 1:
        response_code = 500
    else:
        response_code = 200

    response_time = random.randrange(10, 51)

    time.sleep((response_time + time.time() - beginning) / 1000)

    database[cf.COLLECTION].insert_one({
        cf.OUT_CREATION_DATETIME: creation_datetime.isoformat(),
        cf.PAYLOAD: payload,
        cf.OUT_RESPONSE_TIME: response_time,
        # cf.OUT_CREATION_ROUNDED: creation_datetime - datetime.timedelta(minutes=creation_datetime.minute % 10,
        #                                                                 seconds=creation_datetime.second,
        #                                                                 microseconds=creation_datetime.microsecond),
        cf.OUT_RESPONSE_CODE: response_code,
        cf.OUT_KEY: key
    })

    return {
        "status": response_code,
        "msg": "response"
    }


@app.get(cf.URL_RETRIEVE)
def retrieve(data: RetrievalData):
    """
    Retrieves data inserted from a given date to a given date.
    :param data: class containing two dates as strings.
    """
    date_from = data.Date_from
    date_to = data.Date_to

    date_from = date_parser.parse(date_from)
    date_to = date_parser.parse(date_to) + datetime.timedelta(minutes=1)

    retrieved_info = database[cf.COLLECTION].find({cf.OUT_CREATION_ROUNDED: {"$lt": date_to, "$gte": date_from}})

    print(retrieved_info)

    retrieved_info = retrieved_info.aggregate([{"$count": cf.OUT_CREATION_ROUNDED}])

    # ToDo aggregare retrieved_info per minuti e per chiavi, mantenendo info sul totale di richieste e sugli errori

    return retrieved_info


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=cf.MY_IP, port=cf.MY_PORT)
