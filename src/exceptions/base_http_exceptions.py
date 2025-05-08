from fastapi import HTTPException


class BaseHTTPException(HTTPException):
    description: str
    status_code: int
    exception_code: str