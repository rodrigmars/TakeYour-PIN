
from json import dumps
from bottle import HTTPResponse

def http_response(status_code: int, data: str) -> HTTPResponse:
    return HTTPResponse(status=status_code, body=dumps(data))


def response_builder(code: int, data: dict) -> dict:
    return {"status_code": code,
            "data": data}

