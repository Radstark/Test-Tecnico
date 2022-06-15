import random
from typing import Dict, Union

import config as cf


def ingest(request: Dict[str, Union[int, str]]):
    key = request[cf.KEY]
    payload = request[cf.PAYLOAD]

    if random.randrange(1, 11) == 1:
        response_code = 500
    else:
        response_code = 200


def retrieve(request: Dict[str, str]):
    date_from = request[cf.DATE_FROM]
    date_to = request[cf.DATE_TO]


if __name__ == "__main__":
    ingest({
        cf.KEY: random.randrange(1, 7),
        cf.PAYLOAD: "".join(["a" for _ in range(random.randrange(10, 256))])
    })
