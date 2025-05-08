from fastapi import status

from .base_http_exceptions import BaseHTTPException

class InternalServerError(BaseHTTPException):
    description = "Unhandled error"
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    exception_code = "API_UNHANDLED_ERROR"