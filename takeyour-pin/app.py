from bottle import route, run
from core.user import user
from core.pin import pin

@route('/pin/<email>')
def index(email: str) -> dict:
    
    code: str | None = None

    if user()(email):

        code = pin()()

    return {'pin': code}


run(debug=True, reloader=True, host='localhost', port=8080)
