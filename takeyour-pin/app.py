from bottle import route, run
from core.user import user
from core.pin import pin
from utils import http_response, response_builder


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
