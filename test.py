import datetime
import random

import requests as rq

import config as cf


def post():
    result = rq.post(f"http://{cf.MY_IP}:{cf.MY_PORT}{cf.URL_INGEST}",
                     json={cf.ING_IN_KEY: random.randrange(1, 7),
                           cf.ING_IN_PAYLOAD: "".join(["a" for _ in range(random.randrange(10, 256))])
                           })
    return result.json()


def get():
    result = rq.get(f"http://{cf.MY_IP}:{cf.MY_PORT}{cf.URL_RETRIEVE}",
                    json={cf.RET_IN_DATE_FROM: str(datetime.datetime(2022, 6, 19, 16, 44, 0)),
                          cf.RET_IN_DATE_TO: str(datetime.datetime(2022, 6, 19, 16, 56, 0))
                          })
    return result.json()


if __name__ == "__main__":
    retrieval = get()["msg"]

    for item in retrieval:
        print(item)
