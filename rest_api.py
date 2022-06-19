import random

import requests as rq

import config as cf


def test():
    result = rq.post(f"http://{cf.MY_IP}:{cf.MY_PORT}{cf.URL_INGEST}",
                     json={cf.KEY: random.randrange(1, 7),
                           cf.PAYLOAD: "".join(["a" for _ in range(random.randrange(10, 256))])
                           })
    print(f"==[ result: {result.json()}")


if __name__ == "__main__":
    test()
