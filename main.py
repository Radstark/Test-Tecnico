import datetime
import random
import time

from fastapi import FastAPI

import config as cf
from database import create_database, IngestionData, RetrievalData

# region initialization
app = FastAPI()

database = create_database()
# endregion


# region requests
@app.post(cf.URL_INGEST)
def ingest(data: IngestionData):
    """
    Accepts a request and inserts its data in MongoDB with a fixed date. Response code is randomly 500 10% of the time,
    200 all other times. Takes anywhere between 10 ms and 50 ms, at random.
    :param data: class containing an integer key and a string payload.
    """
    beginning = time.time()
    creation_datetime = datetime.datetime.now()
    key = data.key
    payload = data.payload

    if random.randrange(1, 11) == 1:
        response_code = 500
        is_error = 1
    else:
        response_code = 200
        is_error = 0

    response_time = random.randrange(10, 51)

    time.sleep((response_time + time.time() - beginning) / 1000)

    database[cf.COLLECTION].insert_one({
        cf.ING_OUT_CREATION_DATETIME: creation_datetime,
        cf.ING_OUT_PAYLOAD: payload,
        cf.ING_OUT_RESPONSE_TIME: response_time,
        cf.ING_OUT_RESPONSE_CODE: response_code,
        cf.ING_OUT_KEY: key,
        cf.ING_OUT_CREATION_ROUNDED: creation_datetime - datetime.timedelta(minutes=creation_datetime.minute % 1,
                                                                            seconds=creation_datetime.second,
                                                                            microseconds=creation_datetime.microsecond),
        cf.ING_OUT_IS_ERROR: is_error
    })

    return {
        "status": response_code,
        "msg": "response"
    }


@app.get(cf.URL_RETRIEVE)
def retrieve(data: RetrievalData):
    """
    Retrieves data inserted from a given date to a given date, grouping it by key and rounded creation date, and
    adding information about total time taken for each key-date pair, total requests for each key-date pair, and total
    errors for each key-date pair.
    Result is then reformatted for better readability, separating the key-value pair into the first and last keys.
    :param data: class containing two dates as strings.
    """
    date_from = datetime.datetime.fromisoformat(data.Date_from)
    date_to = datetime.datetime.fromisoformat(data.Date_to)

    results = database[cf.COLLECTION].aggregate([{
        cf.QUERY_MATCH: {
            cf.ING_OUT_CREATION_DATETIME:
                {cf.QUERY_LESSER_THAN: date_to, cf.QUERY_GREATER_EQUAL: date_from}
        }
    }, {
        cf.QUERY_GROUP: {
            "_id": {
                cf.RET_OUT_KEY: f"${cf.ING_OUT_KEY}",
                cf.RET_OUT_CREATION_DATE: f"${cf.ING_OUT_CREATION_ROUNDED}"
            },
            cf.RET_OUT_TOTAL_TIME: {cf.QUERY_SUM: f"${cf.ING_OUT_RESPONSE_TIME}"},
            cf.RET_OUT_TOTAL_REQUESTS: {cf.QUERY_SUM: 1},
            cf.RET_OUT_TOTAL_ERRORS: {cf.QUERY_SUM: f"${cf.ING_OUT_IS_ERROR}"}
        }
    }])

    to_return = []
    for result in results:
        to_return.append({
            cf.RET_OUT_KEY: result["_id"][cf.RET_OUT_KEY],
            cf.RET_OUT_TOTAL_TIME: result[cf.RET_OUT_TOTAL_TIME],
            cf.RET_OUT_TOTAL_REQUESTS: result[cf.RET_OUT_TOTAL_REQUESTS],
            cf.RET_OUT_TOTAL_ERRORS: result[cf.RET_OUT_TOTAL_ERRORS],
            cf.RET_OUT_CREATION_DATE: result["_id"][cf.RET_OUT_CREATION_DATE]
        })

    to_return = list(sorted(sorted(to_return, key=lambda d: d[cf.RET_OUT_KEY]),
                            key=lambda d: d[cf.RET_OUT_CREATION_DATE]))

    return {
        "status": 200,
        "msg": to_return
    }


# endregion


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=cf.MY_IP, port=cf.MY_PORT)
