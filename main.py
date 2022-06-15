import random
from typing import Dict, Union
from fastapi import FastAPI

import config as cf


app = FastAPI()


@app.post(cf.URL_INGEST)
def ingest(request: Dict[str, Union[int, str]]):
    """
    Accepts a request and inserts its data in MongoDB with a fixed date. Response code is randomly 500 10% of the time,
    200 all other times. Takes anywhere between 10 ms and 50 ms, at random.
    :param request: dictionary containing an integer key and a string payload.
    """
    key = request[cf.KEY]
    payload = request[cf.PAYLOAD]

    if random.randrange(1, 11) == 1:
        response_code = 500
    else:
        response_code = 200


@app.get(cf.URL_RETRIEVE)
def retrieve(request: Dict[str, str]):
    """
    Retrieves data inserted from a given date to a given date.
    :param request: dictionary containing two dates as strings.
    """
    date_from = request[cf.DATE_FROM]
    date_to = request[cf.DATE_TO]


if __name__ == "__main__":
    ingest({
        cf.KEY: random.randrange(1, 7),
        cf.PAYLOAD: "".join(["a" for _ in range(random.randrange(10, 256))])
    })
