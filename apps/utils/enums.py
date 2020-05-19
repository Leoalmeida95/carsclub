from enum import Enum


class EStatus_Code(Enum):
    OK = 200
    DATA_INVALID = 422
    EXCEPTION = 500
    NOT_FOUND = 404
    BAD_REQUEST = 400
