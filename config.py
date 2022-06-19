# region urls
URL_INGEST = "/api/v1/ingest"
URL_RETRIEVE = "/api/v1/retrieve"
# endregion

# region ingest
ING_IN_KEY = "key"
ING_IN_PAYLOAD = "payload"
# endregion

# region ingestion output
ING_OUT_CREATION_DATETIME = "Creation_datetime"
ING_OUT_CREATION_ROUNDED = "Creation_time_rounded"
ING_OUT_PAYLOAD = "Payload"
ING_OUT_RESPONSE_TIME = "Response_time"
ING_OUT_RESPONSE_CODE = "Response_code"
ING_OUT_KEY = "Key"
ING_OUT_IS_ERROR = "Is_error"
# endregion

# region retrieve
RET_IN_DATE_FROM = "Date_from"
RET_IN_DATE_TO = "Date_to"
# endregion

# region retrieval output
RET_OUT_KEY = "key"
RET_OUT_CREATION_DATE = "creation_datetime"
RET_OUT_TOTAL_TIME = "total_response_time_ms"
RET_OUT_TOTAL_REQUESTS = "total_requests"
RET_OUT_TOTAL_ERRORS = "total_errors"
# endregion

# region mongodb
DATABASE = "test_tecnico"
USERNAME = "test_tecnico"
PASSWORD = "test_tecnico_123"
HOST = "cluster0.8jbqvyu.mongodb.net/?retryWrites=true&w=majority"
CONNECTION_STRING = f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOST}"
COLLECTION = "test_tecnico"
# endregion

# region local machine
MY_IP = "localhost"
MY_PORT = 8000
# endregion

# region mongodb queries
QUERY_MATCH = "$match"
QUERY_GROUP = "$group"
QUERY_SUM = "$sum"
QUERY_LESSER_THAN = "$lt"
QUERY_GREATER_EQUAL = "$gte"
# endregion
