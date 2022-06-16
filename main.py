import datetime
import random
import time
from typing import Dict, Union

from fastapi import FastAPI

import config as cf
from database import create_database

app = FastAPI()

database = create_database()


@app.post(cf.URL_INGEST)
def ingest(request: Dict[str, Union[int, str]]):
    """
    Accepts a request and inserts its data in MongoDB with a fixed date. Response code is randomly 500 10% of the time,
    200 all other times. Takes anywhere between 10 ms and 50 ms, at random.
    :param request: dictionary containing an integer key and a string payload.
    """
    beginning = time.time()
    creation_datetime = datetime.datetime.now().isoformat()
    key = request[cf.KEY]
    payload = request[cf.PAYLOAD]

    if random.randrange(1, 11) == 1:
        response_code = 500
    else:
        response_code = 200

    response_time = random.randrange(10, 51)

    time.sleep(response_time + time.time() - beginning)

    database[cf.SERVER_TAB].insert_one({
        cf.OUT_CREATION_DATETIME: creation_datetime,
        cf.PAYLOAD: payload,
        cf.OUT_RESPONSE_TIME: response_time,
        cf.OUT_RESPONSE_CODE: response_code,
        cf.OUT_KEY: key
    })

    return {
        "status": response_code,
        "msg": "response"
    }


@app.get(cf.URL_RETRIEVE)
def retrieve(request: Dict[str, str]):
    """
    Retrieves data inserted from a given date to a given date.
    :param request: dictionary containing two dates as strings.
    """
    date_from = request[cf.DATE_FROM]
    date_to = request[cf.DATE_TO]


if __name__ == "__main__":
    # import uvicorn
    #
    # uvicorn.run(app, host="localhost", port=8000)
    ingest({
        cf.KEY: random.randrange(1, 7),
        cf.PAYLOAD: "".join(["a" for _ in range(random.randrange(10, 256))])
    })
