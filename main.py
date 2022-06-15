import random
from typing import Dict, Union
from fastapi import FastAPI

import config as cf


app = FastAPI()


@app.post(cf.URL_INGEST)
def ingest(request: Dict[str, Union[int, str]]):
    key = request[cf.KEY]
    payload = request[cf.PAYLOAD]

    if random.randrange(1, 11) == 1:
        response_code = 500
    else:
        response_code = 200


@app.get(cf.URL_RETRIEVE)
def retrieve(request: Dict[str, str]):
    date_from = request[cf.DATE_FROM]
    date_to = request[cf.DATE_TO]


if __name__ == "__main__":
    ingest({
        cf.KEY: random.randrange(1, 7),
        cf.PAYLOAD: "".join(["a" for _ in range(random.randrange(10, 256))])
    })
