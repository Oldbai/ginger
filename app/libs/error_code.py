from werkzeug.exceptions import HTTPException

from app.libs.error import APIException


class Success(APIException):
    code = 200
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = "sorry, we made a mistake."
    error_code = 999


class ClientTypeError(APIException):
    # 400,401,403,404
    # 500,502
    # 200 201 202,204
    # 301,302
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = "invalid parameter"
    error_code = 1000
