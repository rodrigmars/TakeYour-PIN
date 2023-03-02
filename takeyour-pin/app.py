
from json import dumps
from bottle import route, run, HTTPResponse
from core.user import user
from core.pin import pin


def http_response(status_code: int, data: str) -> HTTPResponse:
    return HTTPResponse(status=status_code, body=dumps(data))


def response_builder(code: int, data: dict) -> dict:
    return {"status_code": code,
            "data": data}


@route('/pin/<email>')
def index(email: str):

    response: dict = {}
    code: str | None = None

    try:
        if user()(email):

            code = pin()()

        response.update(response_builder(200, {'pin': code}))

    except Exception:
        response.update(response_builder(500, {'error': "Unknown error"}))
    finally:
        return http_response(**response)


if __name__ == "__main__":

    run(debug=True, reloader=True, host='localhost', port=8080)
