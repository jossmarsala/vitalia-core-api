from fastapi import status

from .base_http_exceptions import BaseHTTPException

class NotFound(BaseHTTPException):
    description = "No encontrado"
    status_code = status.HTTP_404_INTERNAL_SERVER_ERROR
    exception_code = "API_RESOURCE_NOT_FOUND"