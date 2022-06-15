import random
from typing import Dict, Union


def ingest(request: Dict[str, Union[int, str]]):
    key = request["key"]
    payload = request["payload"]

    if random.randrange(1, 11) == 1:
        response_code = 500
    else:
        response_code = 200




def retrieve():
    pass


if __name__ == "__main__":
    ingest({
        "key": random.randrange(1, 7),
        "payload": "".join(["a" for _ in range(random.randrange(10, 256))])
    })
